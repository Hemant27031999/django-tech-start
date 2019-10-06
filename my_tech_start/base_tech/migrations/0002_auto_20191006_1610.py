# Generated by Django 2.2.5 on 2019-10-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_tech', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCache',
        ),
        migrations.AddField(
            model_name='orders',
            name='id',
            field=models.AutoField(auto_created=True, default=23, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='phone_no',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
