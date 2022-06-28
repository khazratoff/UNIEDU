# Generated by Django 4.0.5 on 2022-06-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_skill_owner_profile_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skill',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(blank=True, null=True, to='users.skill'),
        ),
    ]