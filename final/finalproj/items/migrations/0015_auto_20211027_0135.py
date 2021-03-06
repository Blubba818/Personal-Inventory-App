# Generated by Django 3.2.8 on 2021-10-27 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20211027_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.room'),
        ),
    ]
