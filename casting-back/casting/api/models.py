from django.db import models

# Create your models here.




class Castings(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo: models.ImageField(upload_to='imgs/', blank=True, null=True)



def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'photo': self.photo.url
    }

def __str__(self):
    return self.name