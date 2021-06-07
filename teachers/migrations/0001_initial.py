# Generated by Django 3.2.4 on 2021-06-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=80)),
                ('age', models.IntegerField(default=42)),
                ('subject', models.CharField(max_length=120)),
                ('experience', models.TextField(max_length=500)),
            ],
        ),
    ]
