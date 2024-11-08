# Generated by Django 4.2.7 on 2024-10-29 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ats_app', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferred_location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ats_app.user'),
        ),
    ]
