# Generated by Django 4.0.3 on 2022-03-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
