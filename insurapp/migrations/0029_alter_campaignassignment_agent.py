# Generated by Django 5.1.1 on 2025-01-01 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurapp', '0028_campaign_assigned_agents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignassignment',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='insurapp.agent'),
        ),
    ]
