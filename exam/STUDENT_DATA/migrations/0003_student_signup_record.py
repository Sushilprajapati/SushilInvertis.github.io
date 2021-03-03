# Generated by Django 3.0.5 on 2020-06-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STUDENT_DATA', '0002_auto_20200603_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_signup_record',
            fields=[
                ('college_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('college_name', models.CharField(max_length=20)),
                ('semester', models.IntegerField(max_length=1)),
                ('Email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
