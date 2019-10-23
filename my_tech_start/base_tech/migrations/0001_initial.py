# Generated by Django 2.2.5 on 2019-10-23 16:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorizedProducts',
            fields=[
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_price', models.IntegerField()),
                ('product_rating', models.FloatField()),
                ('product_descp', models.CharField(max_length=255)),
                ('product_imagepath', models.CharField(default='media/images/clothing.png', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.IntegerField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=255)),
                ('categoryImagePath', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cells',
            fields=[
                ('Cell_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Cell_lat', models.FloatField()),
                ('Cell_long', models.FloatField()),
                ('no_vendor', models.IntegerField()),
                ('city', models.CharField(default='Roorkee', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Boys',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('del_boy_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='I', max_length=20)),
                ('total_no_orders', models.IntegerField()),
                ('current_no_orders', models.IntegerField()),
                ('busy', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=255)),
                ('lat', models.FloatField(default=28.33)),
                ('long', models.FloatField(default=77.88)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='indep_Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=30)),
                ('landmark', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('phone_no', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('vendor_id', models.CharField(max_length=100, unique=True)),
                ('vendor_lat', models.FloatField()),
                ('vendor_long', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='I', max_length=20)),
                ('total_no_orders', models.IntegerField(default=0)),
                ('current_no_orders', models.IntegerField(default=0)),
                ('busy', models.CharField(blank=True, max_length=20, null=True)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.Cells')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='001', max_length=255)),
                ('vendor_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.Vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribed_Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorder_id', models.CharField(default=uuid.uuid4, max_length=100)),
                ('delivery_time', models.TimeField(verbose_name='Delivery time')),
                ('delivery_dates', models.CharField(max_length=200)),
                ('delivery_month', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('E', 'Expired')], default='A', max_length=20)),
                ('cust_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_long', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.RegUser')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_tech.CategorizedProducts')),
                ('vendor_phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base_tech.Vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Serving_Vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=500)),
                ('phone_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.Vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default=uuid.uuid4, max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Order date')),
                ('order_time', models.TimeField(auto_now_add=True, verbose_name='Order time')),
                ('address', models.CharField(max_length=500)),
                ('vendor_phone', models.CharField(blank=True, max_length=500, null=True)),
                ('delboy_type', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary')], default='S', max_length=50)),
                ('order_status', models.CharField(choices=[('D', 'Delivered'), ('A', 'Active')], default='A', max_length=50)),
                ('cust_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_long', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.RegUser')),
                ('delivery_boy_phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base_tech.Delivery_Boys')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_tech.CategorizedProducts')),
            ],
        ),
        migrations.CreateModel(
            name='Deliverying_Boys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=500)),
                ('phone_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.Delivery_Boys')),
                ('vendor_phone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_tech.Vendors')),
            ],
        ),
        migrations.AddField(
            model_name='categorizedproducts',
            name='under_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_tech.Category'),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('house_no', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=30)),
                ('landmark', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('phone_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_tech.RegUser')),
            ],
        ),
    ]
