# Generated by Django 4.1 on 2024-02-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_user_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_photo',
            field=models.ImageField(blank=True, null=True, upload_to='car_photos/'),
        ),
    ]
