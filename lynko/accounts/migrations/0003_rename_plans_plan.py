# Generated by Django 4.1.7 on 2024-01-11 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_plans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plans',
            new_name='Plan',
        ),
    ]
