# Generated by Django 2.2.5 on 2019-10-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_tech', '0003_cells_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_boys',
            name='lat',
            field=models.FloatField(default=28.33),
        ),
        migrations.AddField(
            model_name='delivery_boys',
            name='long',
            field=models.FloatField(default=77.88),
        ),
    ]
