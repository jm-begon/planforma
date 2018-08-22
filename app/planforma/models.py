from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)
    name_fr = 'Axes'

    def __str__(self):
        return "[Axe] {}".format(self.name)

    class Meta:
        ordering = ('id',)


class Training(models.Model):
    name = models.CharField(max_length=50)
    name_fr = 'Formations'

    def __str__(self):
        return "[Formation] {}".format(self.name)

    class Meta:
        ordering = ('id',)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ManyToManyField(Field)
    advices = models.CharField(max_length=1024)
    name_fr = 'Compétences'

    def get_fields(self):
        return self.fields.all()

    def __str__(self):
        return "[Comp.] {}".format(self.name)

    class Meta:
        ordering = ('id',)


class Module(models.Model):
    name = models.CharField(max_length=50)
    training = models.ForeignKey(Training, on_delete=models.PROTECT)
    skills = models.ManyToManyField(Skill)
    name_fr = 'Modules'

    def get_skills(self):
        return self.skills.all()

    def __str__(self):
        return "[Module] {}".format(self.name)

    class Meta:
        ordering = ('name', 'training')


class Criterion(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)
    name_fr = 'Critères'

    def get_skills(self):
        return self.skills.all()

    def __str__(self):
        return "[Critère] {}".format(self.name)

    class Meta:
        ordering = ('name',)