# Generated by Django 4.0.4 on 2022-05-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('-updated', '-created')},
        ),
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='car',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
