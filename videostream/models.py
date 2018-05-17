from django.db import models



class Session(models.Model):
    session_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.session_id



