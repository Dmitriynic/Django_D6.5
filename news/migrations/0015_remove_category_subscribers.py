# Generated by Django 3.2.9 on 2021-11-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_category_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
    ]