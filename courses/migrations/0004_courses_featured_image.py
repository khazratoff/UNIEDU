# Generated by Django 4.0.5 on 2022-06-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
