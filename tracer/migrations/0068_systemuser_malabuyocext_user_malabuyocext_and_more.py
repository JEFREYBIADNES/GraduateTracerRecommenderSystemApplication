# Generated by Django 4.1.1 on 2022-12-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0067_user_job_sent_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='malabuyocExt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='malabuyocExt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='school',
            field=models.CharField(blank=True, choices=[('Argao Campus', 'Argao Campus'), ('Barili Campus', 'Barili Campus'), ('Carmen Campus', 'Carmen Campus'), ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'), ('Daanbantayan Campus', 'Daanbantayan Campus'), ('Danao Campus', 'Danao Campus'), ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'), ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'), ('Malabuyoc Extension Campus', 'Malabuyoc Extension Campus'), ('Main Campus', 'Main Campus'), ('Moalboal Campus', 'Moalboal Campus'), ('Naga Extension Campus', 'Naga Extension Campus'), ('Oslob Extension Campus', 'Oslob Extension Campus'), ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'), ('San Fernando Extension Campus', 'San Fernando Extension Campus'), ('San Francisco Campus', 'San Francisco Campus'), ('Tuburan Campus', 'Tuburan Campus')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, choices=[('Argao Campus', 'Argao Campus'), ('Barili Campus', 'Barili Campus'), ('Carmen Campus', 'Carmen Campus'), ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'), ('Daanbantayan Campus', 'Daanbantayan Campus'), ('Danao Campus', 'Danao Campus'), ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'), ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'), ('Malabuyoc Extension Campus', 'Malabuyoc Extension Campus'), ('Main Campus', 'Main Campus'), ('Moalboal Campus', 'Moalboal Campus'), ('Naga Extension Campus', 'Naga Extension Campus'), ('Oslob Extension Campus', 'Oslob Extension Campus'), ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'), ('San Fernando Extension Campus', 'San Fernando Extension Campus'), ('San Francisco Campus', 'San Francisco Campus'), ('Tuburan Campus', 'Tuburan Campus')], max_length=100, null=True),
        ),
    ]
