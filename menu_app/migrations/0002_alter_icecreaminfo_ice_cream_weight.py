# Generated by Django 5.1.5 on 2025-02-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreaminfo',
            name='ice_cream_weight',
            field=models.IntegerField(default=None, max_length=16, null=True),
        ),
    ]
