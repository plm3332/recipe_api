# Generated by Django 3.1.4 on 2021-05-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(default='0', max_length=120),
        ),
    ]
