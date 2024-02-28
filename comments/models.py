from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        help_text="The user who posted the comment",
        verbose_name="Owner"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        help_text="The post which the comment belongs to",
        verbose_name="Post"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    content = models.TextField(help_text="The content of the comment")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']

    def __str__(self):
        return self.content
