# Generated by Django 3.2b1 on 2021-06-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randevu', '0003_alter_randevu_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevu',
            name='boy',
            field=models.IntegerField(default=1),
        ),
    ]