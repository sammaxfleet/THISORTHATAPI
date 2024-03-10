from django.db import models
from django.contrib.auth.models import User

class ContactForm(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        help_text="Contact User",
        verbose_name="User",
        null=True,
        blank=True
    )
    reason = models.CharField(
        max_length=150,
        blank=True,
        help_text="Reason for contact",
        verbose_name="Reason"
    )
    email = models.CharField(
        max_length=150,
        blank=True,
        help_text="Email of the user making the contact",
        null=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.reason
