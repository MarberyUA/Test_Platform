from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime
from Test.models import Test


# Create your models here.

date = str(datetime.today())
date = date[0:10]


class User(AbstractUser):
    """Redefined abstract user"""

    email = models.EmailField(max_length=30, null=True, unique=True,)
    username = models.CharField(max_length=20, blank=True, unique=True)
    profile_photo = models.ImageField(upload_to='profiles_photo', blank=True)
    birthday = models.DateField(default=date, auto_now_add=False)
    personal_description = models.TextField(default='', blank=True)
    verified = models.BooleanField(default=False, blank=True)


    @property
    def get_absolute_image_url(self):
        return '%s' % (self.profile_photo.url)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email
