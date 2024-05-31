from django.db import models

# Create your models here.


class Casting(models.Model):
    name = models.CharField(max_length=300, default="")
    description = models.TextField(blank=True)
    photo = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    def to_json(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'photo': self.photo
    }

class Position(models.Model):
    name = models.CharField(max_length=300)
    requirements = models.TextField()
    casting = models.ForeignKey(Casting, related_name='positions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    def to_json(self):
        return {
        'id': self.id,
        'name': self.name,
        'requirements': self.requirements,
        'casting': self.casting,
    }


class Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth_day = models.IntegerField()
    date_of_birth_month = models.IntegerField()
    date_of_birth_year = models.IntegerField()
    # nationality = models.CharField(max_length=50)
    # email = models.EmailField()
    # phone = models.CharField(max_length=20)
    # instagram = models.CharField(max_length=100)
    # facebook = models.CharField(max_length=100)
    # tiktok = models.CharField(max_length=100)
    # profession = models.CharField(max_length=200)
    # language_kz = models.BooleanField(default=False)
    # language_eng = models.BooleanField(default=False)
    # language_rus = models.BooleanField(default=False)
    # other_languages = models.CharField(max_length=100, blank=True)
    # skills = models.CharField(max_length=300)
    # about_me = models.TextField()
    # photo = models.ImageField(upload_to='photos/', blank=True)
    # video = models.FileField(upload_to='videos/', blank=True)
    # appearance_type = models.CharField(max_length=20)
    # weight = models.FloatField()
    # height = models.FloatField()
    # clothing_size = models.CharField(max_length=10)
    # eye_color = models.CharField(max_length=50)
    # hair_color = models.CharField(max_length=50)
    # individual_features = models.TextField()
    # position = models.ForeignKey(Position, related_name='positions', on_delete=models.CASCADE)

    def __str__(self) -> str:
            return f"{self.id} - applicant"
    

    # we will need this json only to represent some of the applicants in the home/about pages
    def to_json(self):
        return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'gender': self.gender,
        'date_of_birth': f'{self.date_of_birth_year}-{self.date_of_birth_month}-{self.date_of_birth_day}',
        # 'nationality': self.nationality,

    }

class Ad(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.TextField()

    def __str__(self) -> str:
        return f'{self.id} {self.title}'

    def to_json(self):
        return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'photo': self.photo
    }


class ApplicantToPosition(models.Model):
    applicant = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="positions", blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="applicants", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.applicant} - {self.position}"

    def to_json(self):
        return {
        'id': self.id,
        'applicant': self.applicant,
        'position': self.position
    }