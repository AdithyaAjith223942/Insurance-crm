# Generated by Django 5.1.1 on 2024-12-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurapp', '0006_remove_client_created_at_client_aadhar_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
