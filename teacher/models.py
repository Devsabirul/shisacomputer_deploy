from django.db import models

# Create your models here.


class Teachers_info(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
