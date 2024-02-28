from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE,
        help_text="The owner of the profile",
        verbose_name="Owner"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    name = models.CharField(
        max_length=150, blank=True,
        help_text="Name of the Profile",
        verbose_name="Name"
    )
    content = models.TextField(
        blank=True,
        help_text="Bio of the profile",
        verbose_name="Bio"
    )
    image = models.ImageField(
        upload_to='images/', default='../default_profile_image_wgl62u',
        help_text="Profile Image of the user's profile",
        verbose_name="Profile Image"
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
