# Generated by Django 4.2 on 2023-04-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Enter name of the product', max_length=50),
        ),
    ]