# Generated by Django 5.1.1 on 2024-12-31 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurapp', '0025_alter_campaign_campaign_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='assigned_agents',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='campaign_id',
        ),
        migrations.AddField(
            model_name='campaign',
            name='agent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='insurapp.agent'),
        ),
    ]
