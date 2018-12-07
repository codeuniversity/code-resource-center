# Generated by Django 2.1.2 on 2018-12-03 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('departments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department')),
            ],
        ),
        migrations.RemoveField(
            model_name='expertise',
            name='current_profile',
        ),
        migrations.RemoveField(
            model_name='expertise',
            name='departments',
        ),
        migrations.DeleteModel(
            name='Expertise',
        ),
    ]
