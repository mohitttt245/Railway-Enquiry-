# Generated by Django 4.2.2 on 2023-07-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Railway_app', '0013_rename_first_name_passenger_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='card_holder_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='passenger',
            name='card_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='passenger',
            name='train_name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
