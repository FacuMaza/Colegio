# Generated by Django 4.2 on 2024-05-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcolegio', '0006_remove_mate_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estu',
            name='id',
            field=models.AutoField(db_column='user_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mate',
            name='id',
            field=models.AutoField(db_column='user_materia', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prof',
            name='id',
            field=models.AutoField(db_column='user_prof', primary_key=True, serialize=False),
        ),
    ]
