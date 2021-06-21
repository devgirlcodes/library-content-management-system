# Generated by Django 3.1.5 on 2021-06-18 20:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Frequency')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add a genre (e.g. Sports, Travel etc.)', max_length=20, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Publication Name')),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddMagazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessionID', models.PositiveIntegerField(unique=True, verbose_name='Accession ID')),
                ('date_of_entry', models.DateField(default=datetime.date.today, verbose_name='Date of Entry')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('subscription_no', models.CharField(max_length=200, null=True, unique=True, verbose_name='Subscription Number')),
                ('subscription_fee', models.PositiveIntegerField(null=True, verbose_name='Subscription Fee')),
                ('subs_start_date', models.DateField(default=datetime.date.today, verbose_name='Subscription starts on')),
                ('subs_end_date', models.DateField(null=True, verbose_name='Subscription ends on')),
                ('frequency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazines.frequency')),
                ('genre', models.ManyToManyField(help_text='Add genre for this magazine', to='magazines.Genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazines.language')),
                ('publication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazines.publication')),
            ],
            options={
                'verbose_name': 'Magazine',
            },
        ),
    ]