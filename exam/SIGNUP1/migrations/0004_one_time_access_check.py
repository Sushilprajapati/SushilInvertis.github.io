# Generated by Django 3.0.5 on 2020-06-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIGNUP1', '0003_auto_20200608_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='one_time_access_check',
            fields=[
                ('student_id_user', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('access_check_status', models.IntegerField()),
            ],
        ),
    ]