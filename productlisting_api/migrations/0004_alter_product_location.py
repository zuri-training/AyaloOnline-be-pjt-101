# Generated by Django 3.2.4 on 2021-07-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlisting_api', '0003_alter_product_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.TextField(),
        ),
    ]
