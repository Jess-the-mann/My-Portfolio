# Generated by Django 4.1.6 on 2023-10-08 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryption',
            name='encrypted_message',
            field=models.TextField(null=True),
        ),
    ]
