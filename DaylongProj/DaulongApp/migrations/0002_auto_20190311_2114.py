# Generated by Django 2.0.6 on 2019-03-11 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DaulongApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newrecipemodel',
            name='userLink',
        ),
        migrations.AddField(
            model_name='newusermodel',
            name='confirmPassword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newusermodel',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newusermodel',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newrecipemodel',
            name='creatorOfRecipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
