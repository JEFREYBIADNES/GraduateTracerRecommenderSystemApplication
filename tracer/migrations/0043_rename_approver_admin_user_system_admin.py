# Generated by Django 4.1.1 on 2022-09-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0042_user_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='approver_admin',
            new_name='system_admin',
        ),
    ]