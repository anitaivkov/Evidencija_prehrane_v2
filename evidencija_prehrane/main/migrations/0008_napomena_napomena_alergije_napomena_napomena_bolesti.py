# Generated by Django 4.1.4 on 2022-12-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_obrok_obrok_datum_datum_datum_obroka'),
    ]

    operations = [
        migrations.AddField(
            model_name='napomena',
            name='napomena_alergije',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='napomena',
            name='napomena_bolesti',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
