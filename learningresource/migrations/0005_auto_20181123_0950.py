# Generated by Django 2.1.2 on 2018-11-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningresource', '0004_auto_20181121_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningresource',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
    ]
