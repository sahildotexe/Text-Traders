# Generated by Django 3.1.5 on 2021-01-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_books_academic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image1',
            field=models.ImageField(default='Hello', upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image2',
            field=models.ImageField(blank=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image3',
            field=models.ImageField(blank=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image4',
            field=models.ImageField(blank=True, upload_to='books/'),
        ),
    ]
