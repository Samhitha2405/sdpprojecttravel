# Generated by Django 5.0 on 2024-01-06 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0003_alter_register_profilepicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='profilepicture',
        ),
    ]