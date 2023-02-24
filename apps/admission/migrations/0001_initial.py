# Generated by Django 4.1.4 on 2023-01-06 06:57

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=20, verbose_name='title')),
                ('firstname', models.CharField(db_index=True, max_length=100, verbose_name='First Name')),
                ('lastname', models.CharField(db_index=True, max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=500, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('grade', models.CharField(db_index=True, max_length=100, verbose_name='Class')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50, verbose_name='Gender')),
                ('father', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Father Name')),
                ('mother', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Mother Name')),
                ('gaurdian', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Gaurdian Name')),
                ('adhaar', models.IntegerField(verbose_name='Aadhar')),
                ('domicile', models.IntegerField(verbose_name='Domicile Number')),
                ('photograph', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Photo')),
                ('signature', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Signature')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='UpdatedAt')),
            ],
            options={
                'db_table': 'admission',
            },
        ),
    ]
