# Generated by Django 4.2 on 2023-04-29 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of the product', max_length=20)),
                ('category', models.CharField(blank=True, choices=[('el', 'Electronics'), ('gr', 'Grocery'), ('fu', 'Furniture'), ('bo', 'Books')], help_text='Product Category', max_length=2)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for particular product instance', primary_key=True, serialize=False)),
                ('purchased_on', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
