# Generated by Django 3.1.7 on 2021-03-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('apellido', models.CharField(max_length=75)),
                ('sede', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
