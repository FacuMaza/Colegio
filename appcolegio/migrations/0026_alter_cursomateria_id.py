# Generated by Django 4.2 on 2024-06-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcolegio', '0025_alter_mate_options_alter_cursomateria_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursomateria',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
