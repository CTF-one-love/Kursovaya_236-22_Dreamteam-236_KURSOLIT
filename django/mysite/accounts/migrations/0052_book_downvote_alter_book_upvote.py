# Generated by Django 4.2.6 on 2023-12-10 20:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0051_alter_book_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='downvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]
