# Generated by Django 3.1.2 on 2020-11-05 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0002_auto_20201105_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighbour_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='neighbour_name', to='neighbour.name'),
            preserve_default=False,
        ),
    ]
