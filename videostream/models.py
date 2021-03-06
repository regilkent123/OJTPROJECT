from django.db import models
from userprofile.models import UserProfile
# from django.contrib.auth import get_user_model

# User= get_user_model()


class Session(models.Model):
    session_id = models.CharField(max_length=1000)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id

class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)
    def __str__(self):
        return self.archive_id
