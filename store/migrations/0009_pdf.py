# Generated by Django 3.2 on 2022-01-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_bannerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]