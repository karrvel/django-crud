from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER = (
    ('Erkak', "Erkak"),
    ('Ayol', "Ayol")
)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)
    picture = models.ImageField(upload_to="Users")

    gender = models.CharField(max_length=777, choices=GENDER)

    @property
    def ImageUrl(self):
        try:
            url = self.picture.url
        except:
            url = ""
        return url