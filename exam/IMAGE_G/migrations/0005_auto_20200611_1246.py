# Generated by Django 3.0.5 on 2020-06-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMAGE_G', '0004_auto_20200611_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img_store',
            name='img_add',
        ),
        migrations.AddField(
            model_name='img_store',
            name='pic',
            field=models.ImageField(blank=True, default='/static/login.jpeg', upload_to='pics'),
        ),
    ]