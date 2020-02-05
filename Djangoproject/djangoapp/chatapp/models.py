from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)

    def __str__(self):
        return self.Username
