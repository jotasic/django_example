# Generated by Django 3.2.5 on 2021-07-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
