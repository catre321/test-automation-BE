from django.db import models
from django.contrib.auth.models import User

# Add any custom user profile fields if needed
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add custom fields, for example:
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"