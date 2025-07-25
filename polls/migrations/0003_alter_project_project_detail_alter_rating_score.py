# Generated by Django 4.2.23 on 2025-07-05 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_project_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
