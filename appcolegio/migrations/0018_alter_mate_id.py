# Generated by Django 4.2 on 2024-05-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcolegio', '0017_mate_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mate',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
