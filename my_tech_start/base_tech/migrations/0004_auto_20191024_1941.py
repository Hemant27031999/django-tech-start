# Generated by Django 2.2.5 on 2019-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_tech', '0003_merge_20191024_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_products',
            name='product_id',
            field=models.IntegerField(),
        ),
    ]
