# Generated by Django 4.2.2 on 2023-07-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Railway_app', '0011_remove_passenger_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='payment_status',
            field=models.CharField(choices=[('done', 'Done'), ('not_done', 'Not Done')], default='not_done', max_length=10),
        ),
    ]
