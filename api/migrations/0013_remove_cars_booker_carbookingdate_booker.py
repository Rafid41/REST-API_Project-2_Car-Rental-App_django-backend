# Generated by Django 4.1 on 2024-02-25 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_cars_bookeddatelist_carbookingdate_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='booker',
        ),
        migrations.AddField(
            model_name='carbookingdate',
            name='booker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booker_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
