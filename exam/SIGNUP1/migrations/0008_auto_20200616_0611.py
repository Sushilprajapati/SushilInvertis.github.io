# Generated by Django 3.0.5 on 2020-06-16 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIGNUP1', '0007_auto_20200616_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_signup_record1',
            name='D_O_B',
            field=models.DateField(default=datetime.date(2020, 6, 16)),
        ),
    ]