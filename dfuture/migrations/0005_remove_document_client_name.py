# Generated by Django 3.2.8 on 2021-10-09 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfuture', '0004_alter_documentrequest_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='client_name',
        ),
    ]
