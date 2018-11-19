# Generated by Django 2.1.2 on 2018-11-19 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('description', models.TextField()),
                ('is_free', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=1)),
                ('last_edit_date', models.DateTimeField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LearningResourceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learningresource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningresource.LearningResource')),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserLearningResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learningresource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningresource.LearningResource')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='learningresourcetag',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningresource.Tag'),
        ),
        migrations.AddField(
            model_name='learningresource',
            name='media_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningresource.MediaType'),
        ),
    ]
