# Generated by Django 4.1.3 on 2024-02-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avantgardenapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='grow_time',
            field=models.CharField(max_length=50),
        ),
    ]
