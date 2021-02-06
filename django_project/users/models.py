from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    USER_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField(unique = True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length =250)
    gender = models.CharField(max_length = 6 , choices = USER_GENDER)
    city = models.CharField(max_length = 50)

