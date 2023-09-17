# Generated by Django 4.2.5 on 2023-09-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0002_patient_blood_type_patient_is_online_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default='example@example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default=99999999, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]