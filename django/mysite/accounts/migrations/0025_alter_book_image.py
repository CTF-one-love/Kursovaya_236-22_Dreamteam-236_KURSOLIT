# Generated by Django 4.2.6 on 2023-12-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_order_datecreated_order_status_alter_order_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='defaultbook.png', null=True, upload_to=''),
        ),
    ]
