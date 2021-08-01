# Generated by Django 3.2.5 on 2021-08-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_books_model_login_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('BookName', models.CharField(max_length=100)),
                ('CurrentDate', models.DateField()),
            ],
            options={
                'db_table': 'library_take_book',
            },
        ),
        migrations.CreateModel(
            name='ReturnBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('BookName', models.CharField(max_length=100)),
                ('BookIssuedDate', models.DateField()),
            ],
            options={
                'db_table': 'library_return_book',
            },
        ),
    ]