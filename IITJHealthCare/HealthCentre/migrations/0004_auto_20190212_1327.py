# Generated by Django 2.1.5 on 2019-02-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0003_auto_20190212_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rollNumber',
            field=models.CharField(max_length=8),
        ),
    ]
