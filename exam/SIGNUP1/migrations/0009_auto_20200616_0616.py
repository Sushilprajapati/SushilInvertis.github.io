# Generated by Django 3.0.5 on 2020-06-16 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SIGNUP1', '0008_auto_20200616_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_signup_record1',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2020, 6, 16, 6, 16, 17, 313304, tzinfo=utc)),
        ),
    ]
