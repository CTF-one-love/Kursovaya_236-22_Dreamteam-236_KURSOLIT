# Generated by Django 4.2.6 on 2023-12-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_remove_order_review_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(max_length=500, null=True),
        ),
    ]