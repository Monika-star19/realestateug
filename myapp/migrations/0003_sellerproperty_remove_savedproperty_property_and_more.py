# Generated by Django 5.1 on 2024-09-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_property_savedproperty_delete_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sellerproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('property_type', models.CharField(max_length=100)),
                ('bedrooms', models.CharField(max_length=2)),
                ('bathrooms', models.CharField(max_length=2)),
                ('floors', models.CharField(max_length=2)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=10)),
                ('built', models.CharField(max_length=10)),
                ('parking', models.CharField(max_length=5)),
                ('ready', models.CharField(max_length=5)),
                ('furnished', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=5)),
                ('maintenance', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=20)),
                ('hear', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='savedproperty',
            name='property',
        ),
        migrations.RemoveField(
            model_name='savedproperty',
            name='user',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='SavedProperty',
        ),
    ]
