# Generated by Django 3.2.21 on 2024-03-05 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_fashion_inspiration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fashion_inspiration',
            field=models.TextField(blank=True, help_text='Optional field for fashion inspiration related to the post.', null=True, verbose_name='Fashion Inspiration'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'), ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'), ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'), ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'), ('walden', 'Walden'), ('xpro2', 'X-pro II')], default='normal', help_text='Choose a filter for the post image.', max_length=32, verbose_name='Image Filter'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(help_text='The user who owns this post.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]
