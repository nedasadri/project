from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class MyUserManager(BaseUserManager):

    def create_user(self, username, password = None):
        user = self.model(username = username)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, username, password = None):

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):

    username =  models.EmailField(unique = True)
    teacher = models.BooleanField(default = False)
    code = models.DecimalField(max_digits = 10, decimal_places = 0, default = 0)

    is_staff = models.BooleanField( default = False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Film(models.Model):
    film = models.FileField(upload_to='films')


class Tamrin(models.Model):
    matn = models.TextField()
    time = models.CharField(max_length = 250)

    def __str__(self):
        return self.text

class Ersal(models.Model):
    student = models.ForeignKey(MyUser, on_delete = models.PROTECT, related_name = 'ersalha')
    Tamrin = models.ForeignKey(Tamrin, on_delete = models.PROTECT, related_name = 'ersalha')
    file = models.FileField(upload_to = 'uploads')
    nomre = models.PositiveIntegerField(default = None, null = True, blank = True)
    time = models.DateField(default = timezone.now)

    def __str__(self):
        return self.time
