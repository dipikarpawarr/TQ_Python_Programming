# Generated by Django 3.2.5 on 2021-08-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_Up_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'sign_up',
            },
        ),
    ]