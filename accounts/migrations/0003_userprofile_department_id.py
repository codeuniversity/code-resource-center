# Generated by Django 2.1.2 on 2018-11-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181120_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department_id',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.Department'),
        ),
    ]