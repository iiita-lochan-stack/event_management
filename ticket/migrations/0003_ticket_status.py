# Generated by Django 5.0.3 on 2024-07-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
