from os import path, remove

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Custom filename
def get_filename(instance, filename):
    name = 'user_images/' + str(instance.user.id)
    extension = '.' + filename.split('.')[-1]
    fullname = path.join(settings.MEDIA_ROOT, name)
    if path.exists(fullname):
        remove(fullname)
    return name + extension


# User Profile Model
class UserProfile(models.Model):
    image = models.ImageField(upload_to=get_filename)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
