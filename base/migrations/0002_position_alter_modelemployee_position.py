# Generated by Django 4.1.7 on 2023-03-22 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='modelemployee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.position'),
        ),
    ]
