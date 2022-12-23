# Generated by Django 4.1.4 on 2022-12-23 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_datum_datum_obroka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datum',
            name='datum_obroka',
        ),
        migrations.AddField(
            model_name='obrok',
            name='obrok_datum',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.datum'),
        ),
    ]
