# Generated by Django 3.1.5 on 2021-08-19 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210817_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransaction',
            name='date_of_transaction',
            field=models.DateField(default=datetime.date(2021, 8, 19), verbose_name='Date Of Transaction'),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='due_back',
            field=models.DateField(default=datetime.date(2021, 9, 2), verbose_name='Due Back Date:'),
        ),
    ]
