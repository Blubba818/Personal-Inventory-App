# Generated by Django 3.2.8 on 2021-11-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0021_auto_20211104_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='images/inventory.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(default='images/closet.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(default='images/rooms.jpg', upload_to='images/'),
        ),
    ]