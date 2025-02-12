# Generated by Django 5.0.3 on 2024-07-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, db_index=True, max_length=255, null=True)),
                ('has_role', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_email_verified', models.BooleanField(default=True)),
                ('is_phone_verified', models.BooleanField(default=True)),
            ],
        ),
    ]
