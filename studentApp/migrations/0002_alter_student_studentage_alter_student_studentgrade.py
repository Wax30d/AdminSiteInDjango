# Generated by Django 4.0.1 on 2022-01-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentAge',
            field=models.IntegerField(default='Enter student age... '),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentGrade',
            field=models.IntegerField(default='Enter student grade... '),
        ),
    ]
