# Generated by Django 3.2.4 on 2021-07-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_auto_20210705_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='group',
        ),
    ]
