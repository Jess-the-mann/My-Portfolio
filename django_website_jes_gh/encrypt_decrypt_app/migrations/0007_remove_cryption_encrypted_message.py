# Generated by Django 4.1.6 on 2023-10-08 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0006_alter_cryption_encrypted_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryption',
            name='encrypted_message',
        ),
    ]
