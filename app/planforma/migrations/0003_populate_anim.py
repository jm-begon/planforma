# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion

from collections import namedtuple

SkillData = namedtuple('SkillData', ['name', 'fields','advices'])
CriterionData = namedtuple('CriterionData', ['name'])
ModuleData = namedtuple('ModuleData', ['name', 'training_name'])

__SKILLS__ = {
    0: SkillData(name="Organiser l'espace (disposer les enfants, placer les animateurs/trices)",
                 fields=["Animation"],
                 advices=""),
    1: SkillData(name="Proposer une activité (bricolage, chant, activité cuisine, grand/petit jeu, histoire, etc.) adaptée au public (âge, sécurité, etc.) et de l'encadrer dans l'apprentissage/la réalisation de celle-ci",
                 fields=["Animation"],
                 advices=""),
    2: SkillData(name="Rendre son récit vivant et dynamique",
                 fields=["Animation"],
                 advices=""),
    3: SkillData(name="Créer une ambiance autour d'un conte ou d'une histoire",
                 fields=["Animation"],
                 advices=""),
    4: SkillData(name="Inventer des jeux innovants",
                 fields=["Animation"],
                 advices=""),
    5: SkillData(name="Faire vivre la coopération (en différents niveaux) dans ses animations",
                 fields=["Animation"],
                 advices=""),
    6: SkillData(name="Créer des jeux qui respectent les critères des jeux coopératifs",
                 fields=["Animation"],
                 advices=""),
    7: SkillData(name="Présenter le concept de bien-être à Jeunesse & Santé",
                 fields=["Animation"],
                 advices="Est-ce vraiment une compétence?"),
    8: SkillData(name="Créer des animations (notamment des grands jeux) qui développent le bien-être tel que défini par J&S",
                 fields=["Animation"],
                 advices=""),
    9: SkillData(name="Utiliser les outils bien-être/santé mis à disposition par J&S",
                  fields=["Animation"],
                  advices=""),
    10: SkillData(name="Adapter son jeu en fonction du matériel disponible et du lieu",
                  fields=["Animation"],
                  advices=""),
    11: SkillData(name="Adapter le jeu au public (âges, spécificités, etc.)",
                  fields=["Animation"],
                  advices=""),
    12: SkillData(name="Construire un jeu en équipe",
                  fields=["Animation"],
                  advices=""),
    13: SkillData(name="Construire un jeu en pensant à toutes les étapes",
                  fields=["Animation"],
                  advices=""),
    14: SkillData(name="Utiliser la fiche de jeu à bon escient (y compris pour pouvoir expliquer son jeu aux autres animateurs)",
                  fields=["Animation"],
                  advices=""),
    15: SkillData(name="Répartir le groupe en équipes",
                  fields=["Animation"],
                  advices=""),
    16: SkillData(name="Utiliser et enrichir l’univers au service de l’animation, en fonction des décors, avec des chants et selon les personnages",
                  fields=["Animation"],
                  advices=""),
    17: SkillData(name="Organiser sa veillée autour du schéma OV1-OV2-OV3",
                  fields=["Animation"],
                  advices=""),
    18: SkillData(name="Construire des histoires originales qui s’insèrent dans le fil rouge",
                  fields=["Animation"],
                  advices=""),
    19: SkillData(name="Tenir son rôle tout au long de l’animation",
                  fields=["Animation"],
                  advices=""),
    20: SkillData(name="Créer un personnage adapté à la situation (rôle, public…)",
                  fields=["Animation"],
                  advices=""),
}

__MODULES__ = {
    0: ModuleData(name="Veillée", training_name="Noël"),
    1: ModuleData(name="Bricolage", training_name="Noël"),
    2: ModuleData(name="Chant", training_name="Noël"),
    3: ModuleData(name="Cuisine", training_name="??"),
    4: ModuleData(name="Grands jeux de plaine", training_name="??"),
    5: ModuleData(name="Petits jeux (de plaine)", training_name="??"),
    6: ModuleData(name="Jeux dynamisants", training_name="??"),
    7: ModuleData(name="Jeux de connaissance", training_name="Noël"),
    8: ModuleData(name="Raconte moi une histoire", training_name="Carnaval 1e"),
    9: ModuleData(name="Jeux origéniaux", training_name="Carnaval 2e"),
    10: ModuleData(name="Jeux coop", training_name="Carnaval 2e"),
    11: ModuleData(name="Jeux bien-être", training_name="Carnaval 2e"),
    12: ModuleData(name="Jeux", training_name="Noël"),
    13: ModuleData(name="Travail du personnage", training_name="Noël"),
}

__MODULES_2_SKILLS__ = {
    # module id to skill ids
    0: [0, 15, 16, 17, 18],
    1: [1],
    2: [1],
    3: [1],
    4: [1],
    5: [1],
    6: [1],
    7: [1],
    8: [1, 2, 3],
    9: [4],
    10: [5, 6],
    11: [7, 8, 9],
    12: [10, 11, 12, 13, 14],
    13: [19, 20],
}

__CRITERIA__ = {
    0: CriterionData(
        name="Pendant les activités je veille au placement des animateurs par rapport aux enfants."),
    1: CriterionData(
        name="En dehors des activités prévues (ex.: pendant les temps libres, déplacement, temps calme de la sieste, etc.) je propose des activités (grands et patits jeux de plaine, chants, prières, histoires, etc.) adaptées au public (âge, sécurité, etc.) et j'encadre les enfants dans l’apprentissage/la réalisation de celles-ci."),
    2: CriterionData(
        name="Lors des activités prévues, hors grands jeux/veillées (ex. : temps d’équipe, ALS, évaluation, etc.), je propose des activités adaptée au public (âge, sécurité, etc.) et j’encadre les enfants dans la réalisation de celles-ci. J’évite le gaspillage et je n’oublie pas le rangement."),
    3: CriterionData(
        name="je mets en place un dispositif de sécurité adapté à la situation"),
    4: CriterionData(
        name="En toutes circonstances, je donne des consignes adaptées à l’activité proposée et m’assure de leur respect"),
    5: CriterionData(name="je respecte le matériel"),
    6: CriterionData(name="Je crée des jeux inédits, dits \"origéniaux\""),
    7: CriterionData(
        name="Je fais passer des messages et des valeurs grâce à mes animations (bien-être, coopération, etc.)"),
    8: CriterionData(
        name="Je connais le concept de bien-être à Jeunesse et Santé et je sais l’expliquer"),
    9: CriterionData(
        name="je fais passer des messages et des valeurs grâce à mes animations (bien-être, coopération…)"),
    10: CriterionData(
        name="j'adapte mon jeu aux petits imprévus et/ou au terrain (lieu, matériel, intempéries, timing…)"),
    11: CriterionData(
        name="J'adapte mes jeux au public (tranche d'âge et spécificité de mon séjour)"),
    12: CriterionData(
        name="Je participe aux réunions, je suis actif et je donne des idées."),
    13: CriterionData(
        name="Je reste constructif, respecte les idées des autres et favorise le compromis sans imposer mes idées"),
    14: CriterionData(
        name="Je fais apparaître et respecte les différentes étapes d'un jeu dans la préparation de mes jeux (rassembler les enfants, donner les consignes, intro, déroulement, motiver, bouquet final, conclusion, transition...)"),
    15: CriterionData(
        name="Je prépare mes grands jeux en remplissant la fiche de jeu de manière adéquate"),
    16: CriterionData(
        name="Je répartis les enfants en équipe avec des méthodes variées et originales, et si possible adaptées au thème)"),
    17: CriterionData(
        name="Lors de mes différents jeux je propose des éléments qui enrichissent l'univers (création/utilisation des décors, chants adaptés, épreuves en rapport avec le thème…)"),
    18: CriterionData(
        name="Je fais apparaître et respecte les étapes OV1-2-3 dans la préparation de mes veillées (fiches, animations adaptées…)"),
    19: CriterionData(
        name="Les histoires de mes jeux sont en cohérence avec le fil rouge fixé avec l'équipe et permettent aux enfants de se plonger dans l'aventure globale"),
    20: CriterionData(
        name="Je respecte mon personnage (dans tous ses aspects) tout au long de l'animation, y compris pour donner les consignes."),
    21: CriterionData(
        name="Mes déguisements sont un réel atout pour compléter mon personnage."),
    22: CriterionData(name="Au besoin, j'utilise la fiche personnage"),

}

__CRITERIA_2_SKILLS__ = {
    # criteira id to skill ids
    0: [0],
    1: [1], # 2, 3],
    2: [1],
    3: [1],
    4: [1],
    5: [1],
    6: [4],
    7: [5, 6],
    8: [7],
    9: [8, 9],
    10: [10],
    11: [11, 18],
    12: [12],
    13: [12],
    14: [13],
    15: [14],
    16: [15],
    17: [16],
    18: [17],
    19: [18],
    20: [19],
    21: [20],
    22: [20],
}


def fill_in_anim(apps, schema_editor):
    fields_name2id = {}
    Field = apps.get_model("planforma", 'Field')
    for field in Field.objects.all():
        fields_name2id[field.name] = field.id

    trainings_name2inst = {}
    Training = apps.get_model('planforma', 'Training')
    for training in Training.objects.all():
        trainings_name2inst[training.name] = training
    training = Training(name="??")
    trainings_name2inst[training.name] = training
    training.save()

    skills_id_loc2glob = {}
    Skill = apps.get_model('planforma', 'Skill')
    for loc_id, skill_data in __SKILLS__.items():
        skill = Skill(name=skill_data.name, advices=skill_data.advices)
        skill.save()
        skills_id_loc2glob[loc_id] = skill.id
        for field_name in skill_data.fields:
            skill.fields.add(fields_name2id[field_name])
        skill.save()

    Module = apps.get_model('planforma', 'Module')
    for loc_id, module_data in __MODULES__.items():
        module = Module(name=module_data.name,
                        training=trainings_name2inst[module_data.training_name])
        module.save()
        for skill_loc_id in __MODULES_2_SKILLS__[loc_id]:
            module.skills.add(skills_id_loc2glob[skill_loc_id])
        module.save()

    Criterion = apps.get_model('planforma', 'Criterion')
    for loc_id, criterion_data in __CRITERIA__.items():
        criterion = Criterion(name=criterion_data.name)
        criterion.save()
        for skill_loc_id in __CRITERIA_2_SKILLS__[loc_id]:
            criterion.skills.add(skills_id_loc2glob[skill_loc_id])
        criterion.save()


class Migration(migrations.Migration):

    dependencies = [
        ('planforma', '0002_populate_defaults'),
    ]

    operations = [
        migrations.RunPython(fill_in_anim),
    ]
