# Generated by Django 4.0.5 on 2022-06-15 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_delete_users'),
        ('courses', '0006_courses_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
