# Generated by Django 3.1.2 on 2020-11-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0003_profile_neighbourhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='job_description'),
        ),
    ]