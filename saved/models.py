from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Saved(models.Model):
    """
    Saved model, related to 'owner' and 'post'.
    'owner' is a User that saved a Post.
    'post' is a Post that was saved by 'owner'.
    'unique_together' makes sure a user can't 'double save' the same post.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        help_text="The user who saved the post",
        verbose_name="Owner"
    )
    post = models.ForeignKey(
        Post, related_name='saved', on_delete=models.CASCADE,
        help_text="The post being saved",
        verbose_name="Post"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Saved"
        verbose_name_plural = "Saved"
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} saved {self.post}'
