# Generated by Django 3.2 on 2022-01-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_customer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='quantity',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
