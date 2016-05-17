from django.db import models
import django
from django.contrib.auth.models import User
from registration.signals import user_registered
from accounts.forms import UserRegistrationForm

django.setup()

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


def user_registered_callback(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()


user_registered.connect(user_registered_callback)