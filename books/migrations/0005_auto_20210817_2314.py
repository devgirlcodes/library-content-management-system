# Generated by Django 3.1.5 on 2021-08-17 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210625_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransaction',
            name='date_of_transaction',
            field=models.DateField(default=datetime.date(2021, 8, 17), verbose_name='Date Of Transaction'),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='due_back',
            field=models.DateField(default=datetime.date(2021, 8, 31), verbose_name='Due Back Date:'),
        ),
    ]
