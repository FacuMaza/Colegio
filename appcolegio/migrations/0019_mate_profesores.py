# Generated by Django 4.2 on 2024-05-14 16:40

import appcolegio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcolegio', '0018_alter_mate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='mate',
            name='Profesores',
            field=models.CharField(choices=[('1', appcolegio.models.prof), ('2', 'pedro')], default='1', max_length=30),
        ),
    ]
