# Generated by Django 3.0.4 on 2020-03-29 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('textuten', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyukey',
            name='tim',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
