# Generated by Django 2.2 on 2019-10-23 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0006_gallary_gallaryimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallaryimage',
            name='video',
        ),
        migrations.DeleteModel(
            name='Gallary',
        ),
        migrations.DeleteModel(
            name='GallaryImage',
        ),
    ]
