# Generated by Django 4.2.2 on 2023-06-24 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=30, null=True)),
                ('train_no', models.IntegerField(null=True)),
                ('from_city', models.CharField(max_length=30, null=True)),
                ('to_city', models.CharField(max_length=30, null=True)),
                ('departure_time', models.TimeField(null=True)),
                ('arrival_time', models.TimeField(null=True)),
                ('travel_time', models.TimeField(null=True)),
                ('distance', models.IntegerField(null=True)),
                ('img', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('add', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('route', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=15, null=True)),
                ('date', models.DateField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Railway_app.add_train')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Railway_app.register')),
            ],
        ),
        migrations.CreateModel(
            name='Add_route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Railway_app.add_train')),
            ],
        ),
    ]