# Generated by Django 3.2.4 on 2021-06-29 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_group'),
        ('groups', '0002_group_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headed_group', to='students.student'),
        ),
    ]