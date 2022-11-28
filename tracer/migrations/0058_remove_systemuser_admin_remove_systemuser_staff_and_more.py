# Generated by Django 4.1.1 on 2022-09-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0057_systemuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='staff',
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]