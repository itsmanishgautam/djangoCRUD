from django.db import models

# Create your models here.
class formdata(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
