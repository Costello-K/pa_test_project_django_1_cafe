# Generated by Django 4.1.4 on 2022-12-18 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_review_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '22'), (3, '333'), (4, '4444'), (5, '55555')]),
        ),
    ]
