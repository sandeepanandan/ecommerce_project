# Generated by Django 4.0.4 on 2022-06-09 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_conutry_order_country_alter_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='toatal_price',
            new_name='total_price',
        ),
    ]
