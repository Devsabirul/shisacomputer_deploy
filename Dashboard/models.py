from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    registration = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    courses = models.CharField(max_length=200)
    certificate = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
