from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    age = models.IntegerField(blank=True, null=True)
    location = models.CharField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username} from {self.location}"
