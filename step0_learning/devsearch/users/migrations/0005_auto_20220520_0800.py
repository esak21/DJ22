# Generated by Django 3.2.4 on 2022-05-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220520_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
