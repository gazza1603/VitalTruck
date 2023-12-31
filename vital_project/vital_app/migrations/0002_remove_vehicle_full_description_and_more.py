# Generated by Django 4.2.6 on 2023-10-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_app', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='vehicle',
            name='area_available',
            field=models.CharField(default='not set', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(default='available', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='workshop_entry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
