# Generated by Django 3.0.5 on 2020-06-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GALLERY', '0003_remove_add_image_s_img_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_image',
            name='s_img_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
