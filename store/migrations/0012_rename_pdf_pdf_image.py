# Generated by Django 3.2 on 2022-01-07 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_pdf_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdf',
            old_name='pdf',
            new_name='image',
        ),
    ]
