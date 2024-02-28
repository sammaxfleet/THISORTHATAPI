from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        help_text="The user who likes the post",
        verbose_name="Owner"
    )
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE,
        help_text="The post being liked",
        verbose_name="Post"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} likes {self.post}'
