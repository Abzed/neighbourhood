# Generated by Django 3.1.2 on 2020-11-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0002_auto_20201103_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='neighbourhood_name',
            field=models.CharField(choices=[('1', 'Langata'), ('2', 'Dagoretti'), ('3', 'Embakasi'), ('4', 'CBD'), ('5', 'Kasarani'), ('6', 'Kibra'), ('7', 'Westland'), ('8', 'Parkland')], max_length=120),
        ),
    ]