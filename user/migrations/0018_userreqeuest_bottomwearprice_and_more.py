# Generated by Django 4.2.3 on 2023-07-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_userreqeuest_totalprice_alter_userreqeuest_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreqeuest',
            name='bottomwearprice',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userreqeuest',
            name='otherclothesprice',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userreqeuest',
            name='topwearprice',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userreqeuest',
            name='woolenwearprice',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
