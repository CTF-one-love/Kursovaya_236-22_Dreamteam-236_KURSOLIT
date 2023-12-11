# Generated by Django 4.2.6 on 2023-12-10 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(blank=True, max_length=200, null=True)),
                ('query', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]
