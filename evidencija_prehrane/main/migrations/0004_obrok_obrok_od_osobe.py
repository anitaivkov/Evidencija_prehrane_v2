# Generated by Django 4.1.4 on 2022-12-22 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_obrok_obrok_namirnice'),
    ]

    operations = [
        migrations.AddField(
            model_name='obrok',
            name='obrok_od_osobe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.osoba'),
        ),
    ]
