# Generated by Django 3.0.8 on 2020-11-27 13:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_check_requirements', models.TextField()),
                ('commitment_type', models.TextField()),
                ('datetime', models.DateTimeField(blank=True, help_text='Event date')),
                ('description', models.TextField()),
                ('clothing_requirements', models.TextField()),
                ('location', models.TextField()),
                ('personnel_needed', models.IntegerField()),
                ('post_privacy', models.CharField(choices=[('public', 'public'), ('private', 'private'), ('unlisted', 'unlisted')], default='public', max_length=8)),
                ('skills_required', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), size=None)),
                ('title', models.CharField(max_length=60)),
            ],
        ),
    ]