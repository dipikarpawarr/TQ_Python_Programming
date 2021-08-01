# Generated by Django 3.2.5 on 2021-08-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_issuebook_returnbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue_Book_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('BookName', models.CharField(max_length=100)),
                ('IssuedDate', models.DateField()),
                ('ReturnDate', models.DateField()),
            ],
            options={
                'db_table': 'library_take_book',
            },
        ),
        migrations.CreateModel(
            name='Return_Book_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('BookName', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='IssueBook',
        ),
        migrations.DeleteModel(
            name='ReturnBook',
        ),
    ]