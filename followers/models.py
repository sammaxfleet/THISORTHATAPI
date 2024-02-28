from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    'owner' is a User that is following a User.
    'followed' is a User that is followed by 'owner'.
    We need the related_name attribute so that django can differentiate
    between 'owner' and 'followed' who both are User model instances.
    'unique_together' makes sure a user can't 'double follow' the same user.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE,
        help_text="The user who is following another user",
        verbose_name="Follower"
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE,
        help_text="The user who is being followed by another user",
        verbose_name="Followed"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Follower"
        verbose_name_plural = "Followers"
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} follows {self.followed}'
