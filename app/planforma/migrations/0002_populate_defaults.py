# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


def fill_in_defaults(apps, schema_editor):
    Field = apps.get_model("planforma", 'Field')
    for name, long_name in ('Animation', 'Crée et anime'), \
                           ('Bien-être', 'Veille au bien-être'), \
                           ('Engagement', 'Vit un engagement'), \
                           ('Evalue', 'Evalue'), \
                           ("Amusement", "Favorise l'amusement"), \
                           ('Autre', "Fait d'autres trucs"):
        field = Field(name=name, long_name=long_name)
        field.save()

    Training = apps.get_model('planforma', 'Training')
    for name in 'Noël', 'Carnaval 1e', 'Form@ctive 1e', 'Toussaint', \
                'Carnaval 2e', 'Form@ctive 2e':
        training = Training(name=name)
        training.save()


class Migration(migrations.Migration):

    dependencies = [
        ('planforma', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_in_defaults),
    ]
