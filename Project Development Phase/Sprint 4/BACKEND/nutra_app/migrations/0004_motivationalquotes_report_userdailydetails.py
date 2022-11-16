# Generated by Django 4.1.3 on 2022-11-12 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nutra_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('nutra_app', '0003_food_foodcalorieconversionfactor_foodcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivationalQuotes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quote', models.CharField(default='', max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to=nutra_app.models.report_upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDailyDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('calories_morning', models.FloatField(default=0.0)),
                ('calories_afternoon', models.FloatField(default=0.0)),
                ('calories_night', models.FloatField(default=0.0)),
                ('calories_today_total', models.FloatField(default=0.0)),
                ('calories_previous_day', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
