from sqlite3 import IntegrityError
from rest_framework import serializers
from api.models import ApplicantToPosition, Casting, Position, Form, Ad
from django.contrib.auth.models import User

class CastingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300, default="")
    description = serializers.CharField()
    photo = serializers.CharField(max_length=500, allow_blank=True)

    def create(self, validated_data):
        instance = Casting.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            photo = validated_data.get('photo'))
        return instance
    
    def update(self, instance,validated_data ):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.photo = validated_data.get('photo')
        instance.save()
        return instance



class AdSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300, default="")
    description = serializers.CharField()
    photo = serializers.CharField(max_length=500, allow_blank=True)

    def create(self, validated_data):
        instance = Ad.objects.create(
            title = validated_data.get('title'),
            description = validated_data.get('description'),
            photo = validated_data.get('photo'))
        return instance
    
    def update(self, instance,validated_data ):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.photo = validated_data.get('photo')
        instance.save()
        return instance
    



class PositionSerializer(serializers.ModelSerializer):
    casting = CastingSerializer(read_only=True)
    class Meta:
        model = Position
        fields = "__all__"

    def create(self, validated_data):
        casting = self.context['casting']
        return Position.objects.create(casting=casting, **validated_data)
    
    def update(self, instance, validated_data):
        casting = self.context.get('casting', instance.casting)
        instance.name = validated_data.get('name', instance.name)
        instance.requirments = validated_data.get('requirements', instance.requirements)
        instance.casting = casting
        instance.save()
        return instance


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth_day', 'date_of_birth_month', 'date_of_birth_year', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(**validated_data)
   
class ApplicationsSerializer(serializers.ModelSerializer):
    applicant = FormSerializer()
    position = PositionSerializer()
    class Meta:
        model = ApplicantToPosition
        fields = "__all__"

    def create(self, validated_data):
        applicant_data = validated_data.pop('applicant')
        position_data = validated_data.pop('position')

        
        # applicant_instance = Form.objects.get_or_create(**applicant_data)
        try:
            # Retrieve or create Form instance based on provided data
            applicant_instance, created = Form.objects.get_or_create(**applicant_data)
        except Exception as e:
            raise serializers.ValidationError(f"Error fetching or creating Form: {str(e)}")

        # position_instance = Position.objects.get_or_create(**position_data)
        try:
            # Retrieve or create Position instance based on provided data
            position_instance, created = Position.objects.get_or_create(**position_data)
        except Exception as e:
            raise serializers.ValidationError(f"Error fetching or creating Position: {str(e)}")

        

        applicant_to_position_instance = ApplicantToPosition.objects.create(
            applicant=applicant_instance,
            position=position_instance,
            **validated_data
        )

        return applicant_to_position_instance
    
    # def create(self, validated_data):
    #     position_id = validated_data.pop('position_id')  # Assuming you send position_id from frontend
    #     position = Position.objects.get(id=position_id)
    #     validated_data['position'] = position  # Populate position data
    #     return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']