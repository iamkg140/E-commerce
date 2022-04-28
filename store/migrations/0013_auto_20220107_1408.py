# Generated by Django 3.2 on 2022-01-07 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_pdf_pdf_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pdf',
            new_name='Brochure',
        ),
        migrations.AlterModelOptions(
            name='bannerimage',
            options={'verbose_name_plural': '3. BannerImage'},
        ),
        migrations.AlterModelOptions(
            name='brochure',
            options={'verbose_name_plural': '4. Brochure'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Category'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': '6. Contact'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '7. Contact'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '1. Product'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name_plural': '5. Setting'},
        ),
    ]