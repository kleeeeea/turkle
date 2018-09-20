# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('input_csv_fields', jsonfield.fields.JSONField()),
            ],
            options={
                'verbose_name': 'HIT',
            },
        ),
        migrations.CreateModel(
            name='HitAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', jsonfield.fields.JSONField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hits.Hit')),
            ],
            options={
                'verbose_name': 'HIT Assignment',
            },
        ),
        migrations.CreateModel(
            name='HitBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignments_per_hit', models.IntegerField(default=1)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('filename', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': 'HIT batch',
                'verbose_name_plural': 'HIT batches',
            },
        ),
        migrations.CreateModel(
            name='HitTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignments_per_hit', models.IntegerField(default=1)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('filename', models.CharField(max_length=1024)),
                ('form', models.TextField()),
                ('name', models.CharField(max_length=1024)),
                ('fieldnames', jsonfield.fields.JSONField(blank=True)),
            ],
            options={
                'verbose_name': 'HIT template',
            },
        ),
        migrations.AddField(
            model_name='hitbatch',
            name='hit_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hits.HitTemplate'),
        ),
        migrations.AddField(
            model_name='hit',
            name='hit_batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hits.HitBatch'),
        ),
    ]
