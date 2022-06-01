# Generated by Django 4.0.3 on 2022-03-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=25)),
                ('account_type', models.CharField(choices=[('Checking', 'Checking'), ('Savings', 'Savings'), ('Investment', 'Investment')], max_length=15)),
                ('balance', models.BigIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='pref_customer',
            new_name='preferred_customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='zip1',
            new_name='zip',
        ),
    ]