# Generated by Django 4.0 on 2022-02-02 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='email',
            new_name='email_address',
        ),
    ]
