# Generated by Django 5.0 on 2024-01-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_register_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profilepicture',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
