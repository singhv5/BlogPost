# Generated by Django 4.2 on 2023-04-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0003_comment_updated_date_alter_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]