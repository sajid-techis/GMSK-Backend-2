# Generated by Django 4.1.7 on 2023-02-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_form',
            name='email',
            field=models.EmailField(max_length=500, unique=True, verbose_name='Email'),
        ),
    ]
