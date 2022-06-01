# Generated by Django 4.0.3 on 2022-03-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0025_alter_account_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='statement',
        ),
        migrations.AlterField(
            model_name='account',
            name='paper_statement',
            field=models.BooleanField(default=False, help_text='Check box to receive a paper statement '),
        ),
    ]