from rest_framework import serializers
from api.models import Casting, Position, Form, Ad


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


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300, default="")
    requirements = serializers.CharField(max_length=500, allow_blank=True)
   
    def create(self, validated_data):
        instance = Position.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            # casting= CastingSerializer(),
        )
        return instance
    
    def update(self, instance,validated_data ):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        # instance.castingТУТ ТОЖЕ САМОЕ
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
    




class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('first_name', 'last_name', 'gender','date_of_birth_day','date_of_birth_month','date_of_birth_year','nationality',
                  'email','phone','instagram','facebook','tiktok','profession','language_kz','language_eng','language_rus','other_languages',
                  'skills','about_me','photo','video','appearance_type','weight','height','clothing_size','eye_color','hair_color','individual_features')
        

class PositionSerializer2(serializers.ModelSerializer):
    casting = CastingSerializer()
    class Meta:
        model = Position
        fields = ('name', 'requirements', 'casting')
