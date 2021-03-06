# Generated by Django 3.2.4 on 2021-06-29 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(blank=True, max_length=20, null=True)),
                ('a_phno', models.IntegerField(blank=True, null=True)),
                ('a_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('artist_img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_img', models.ImageField(upload_to='media')),
                ('aw_name', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('artist_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(blank=True, max_length=20, null=True)),
                ('c_phno', models.IntegerField(blank=True, null=True)),
                ('c_email', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customerdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('phno', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(blank=True, max_length=20, null=True)),
                ('g_location', models.CharField(blank=True, max_length=20, null=True)),
                ('g_phno', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('delivery_detail', models.CharField(choices=[('Pending', 'Pending'), ('Out of Stock', 'Out of Stock'), ('Delivered', 'Delivered')], default=False, max_length=30, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.artwork')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.order')),
            ],
        ),
        migrations.CreateModel(
            name='Instock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_pieces', models.IntegerField(blank=True, null=True)),
                ('aw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('e_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('e_img', models.ImageField(upload_to='media')),
                ('e_name', models.CharField(blank=True, max_length=20, null=True)),
                ('e_type', models.CharField(blank=True, max_length=20, null=True)),
                ('s_date', models.DateField(blank=True, null=True)),
                ('e_date', models.DateField(blank=True, null=True)),
                ('e_year', models.IntegerField(blank=True, null=True)),
                ('elocation', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('gallery_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.gallery')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='gallery_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artgallery.gallery'),
        ),
    ]
