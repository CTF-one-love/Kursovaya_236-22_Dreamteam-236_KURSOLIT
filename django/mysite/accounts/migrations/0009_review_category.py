# Generated by Django 4.2.6 on 2023-11-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='category',
            field=models.CharField(choices=[('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Knowledge', 'Knowlegde')], max_length=200, null=True),
        ),
    ]
