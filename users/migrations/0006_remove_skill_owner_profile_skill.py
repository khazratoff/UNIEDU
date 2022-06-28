# Generated by Django 4.0.5 on 2022-06-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_skill_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.skill'),
        ),
    ]