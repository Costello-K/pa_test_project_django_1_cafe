# Generated by Django 4.1.4 on 2022-12-26 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_usermessage_alter_userreservation_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.CharField(max_length=200),
        ),
    ]
