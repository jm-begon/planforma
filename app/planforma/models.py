from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)

    def __str__(self):
        return "[Axe] {}".format(self.name)

    class Meta:
        ordering = ('name', 'long_name')


class Skill(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ManyToManyField(Field)
    advices = models.CharField(max_length=1024)

    def __str__(self):
        return "[Comp.] {}".format(self.name)

    class Meta:
        ordering = ('name', 'advices')


class Training(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "[Formation] {}".format(self.name)

    class Meta:
        ordering = ('name',)


class Module(models.Model):
    name = models.CharField(max_length=50)
    training = models.ForeignKey(Training, on_delete=models.PROTECT)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "[Module] {}".format(self.name)

    class Meta:
        ordering = ('name', 'training')


class Criterion(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "{}(name={})".format(self.__class__.__name__, repr(self.name))

    class Meta:
        ordering = ('name',)
