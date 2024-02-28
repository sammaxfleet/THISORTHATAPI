from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Owner',
        help_text='The user who owns this post.'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content',)
    fashion_inspiration = models.TextField(
        null=True, blank=True,
        verbose_name='Fashion Inspiration',
        help_text='Optional field for fashion inspiration related to the post.'
    )
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True,
        verbose_name='Image'
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal',
        verbose_name='Image Filter',
        help_text='Choose a filter for the post image.'
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
