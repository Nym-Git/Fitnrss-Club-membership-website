# Generated by Django 3.1.7 on 2021-07-12 05:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FitnessClub_App', '0004_auto_20210712_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspaymenthistory',
            name='Buying_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userspaymenthistory',
            name='expire_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
