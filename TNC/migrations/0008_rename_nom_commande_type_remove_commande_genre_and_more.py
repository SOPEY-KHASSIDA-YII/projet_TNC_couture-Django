# Generated by Django 5.0.1 on 2024-01-30 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TNC', '0007_commande'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='nom',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='year',
        ),
    ]
