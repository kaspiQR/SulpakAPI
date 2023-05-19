from django.db import models


# Create your models here.
class VerificationEmail(models.Model):
    email = models.EmailField()
    code = models.IntegerField()

    def __str__(self):
        return self.email
