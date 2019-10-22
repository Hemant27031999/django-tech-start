# Generated by Django 2.2.5 on 2019-10-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_tech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBoyOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=500)),
                ('accepted', models.BooleanField()),
                ('del_boy_no', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_tech.Delivery_Boys')),
            ],
        ),
    ]
