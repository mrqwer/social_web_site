# Generated by Django 4.1.2 on 2022-11-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='customuser',
            name='github',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
