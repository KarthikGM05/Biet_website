# Generated by Django 3.0.6 on 2020-05-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0008_auto_20200523_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_science_dept_timetable',
            name='course',
            field=models.CharField(choices=[('BE', 'B.E.'), ('MT', 'M.Tech')], default='BE', max_length=100),
        ),
    ]
