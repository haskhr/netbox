# Generated by Django 3.1b1 on 2020-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0113_nullbooleanfield_to_booleanfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='local_context_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='napalm_args',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
