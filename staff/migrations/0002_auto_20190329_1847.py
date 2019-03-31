# Generated by Django 2.1.7 on 2019-03-29 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timing', '0001_initial'),
        ('staff', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffschedule',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='philDay', to='timing.PhilDay'),
        ),
        migrations.AddField(
            model_name='staffschedule',
            name='staffID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffUserID', to='user.User'),
        ),
    ]
