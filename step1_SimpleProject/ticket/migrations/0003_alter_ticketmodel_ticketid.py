# Generated by Django 4.0.5 on 2022-06-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticketmodel_assigned_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ticketId',
            field=models.CharField(default='COG6133', max_length=25),
        ),
    ]
