from django.db import models

__FIELD__ = (
    ("Animation", "Crée et anime"),
    ("Wellbeing", "Veille au bien-être"),
    ("Commitment", "Vit un engagement"),
    ("Evaluation", "Evalue"),
    ("Fun", "Favorise l'amusement"),
    ("Other", "Fait d'autres trucs")
)

__TRAINING__ = (
    ("Noel", "Noel"),
    ("Carnaval1", "Carnaval 1e"),
    ("Formactive1", "Form@ctive 1e"),
    ("Toussaint", "Toussaint"),
    ("Carnaval2", "Carnval 2e"),
    ("Formactive2", "Form@ctive 2e")
)


class Field(models.Model):
    name = models.CharField(max_length=30, choices=__FIELD__)  # Axe

    def __str__(self):
        return "{}(name={}".format(self.__class__.__name__, repr(self.name))

    class Meta:
        ordering = ('name',)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ManyToManyField(Field)
    advices = models.CharField(max_length=1024)

    def __str__(self):
        return "{}(name={}".format(self.__class__.__name__, repr(self.name))

    class Meta:
        ordering = ('name', 'advices')


class Module(models.Model):
    name = models.CharField(max_length=50)
    training = models.CharField(max_length=50, choices=__TRAINING__) # Formation
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "{}(name={}, training={}".format(self.__class__.__name__,
                                                repr(self.name),
                                                repr(self.training))

    class Meta:
        ordering = ('name', 'training')


class Criterion(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "{}(name={}".format(self.__class__.__name__, repr(self.name))

    class Meta:
        ordering = ('name',)



