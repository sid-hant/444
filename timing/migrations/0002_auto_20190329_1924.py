# Generated by Django 2.1.7 on 2019-03-30 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrivaltime',
            name='licenseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userID', to=settings.AUTH_USER_MODEL),
        ),
    ]
