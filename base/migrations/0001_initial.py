# Generated by Django 4.1.7 on 2023-03-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=20)),
                ('emp_code', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=30)),
            ],
        ),
    ]
