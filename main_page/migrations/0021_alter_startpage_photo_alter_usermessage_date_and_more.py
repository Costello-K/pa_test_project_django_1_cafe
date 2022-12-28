# Generated by Django 4.1.4 on 2022-12-27 15:21

import datetime
from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0020_alter_startpage_photo_alter_usermessage_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startpage',
            name='photo',
            field=models.FileField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 17, 21, 5, 234941)),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 17, 21, 5, 234941)),
        ),
    ]
