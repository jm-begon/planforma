from django.shortcuts import render
from django.http import HttpResponse

from .models import *

from collections import namedtuple


Sticker = namedtuple('Sticker', ['id', 'name', 'components'])

StickerComponent = namedtuple('StickerComponent', ['id', 'name'])

# View for 'Axes' : Category
#     'Axe 1': Sticker
#          'Formations': Category
#               'Noel', ... : StickerComponent


__ADDRESSES__ = {
    Field: 'axes',
    Training: 'formations',
    Skill: 'competences',
    Module: 'modules',
    Criterion: 'criteres'
}


class MainCategory(object):
    def __init__(self, name, address, list):
        self.name = name
        self.address = address
        self.list = list

    @classmethod
    def get_fields(cls, order_by='id'):
        return Field.objects.order_by(order_by)

    @classmethod
    def get_trainings(cls, order_by='id'):
        return Training.objects.order_by(order_by)

    @classmethod
    def get_modules(cls, order_by='id'):
        return Module.objects.order_by(order_by)

    @classmethod
    def get_skills(cls, order_by='fields'):
        return Skill.objects.order_by(order_by)

    @classmethod
    def get_criteria(cls, order_by='id'):
        return Criterion.objects.order_by(order_by)

    @classmethod
    def from_(cls, Model_cls, sticker_list):
        print(Model_cls.name_fr)
        return MainCategory(Model_cls.name_fr, __ADDRESSES__[Model_cls],
                            sticker_list)



class Category(MainCategory):
    def __init__(self, name, address, list, short=False):
        super().__init__(name, address, list)
        self.short = short

    @classmethod
    def from_iterable(cls, iterable, name, address, short=False):
        # components = [StickerComponent(x.id, x.name) for x in iterable]
        components = list(iterable)
        return cls(name=name, address=address, list=components, short=short)

    @classmethod
    def fields(cls, iterable, short=True):
        return cls.from_iterable(iterable, Field.name_fr,
                                 __ADDRESSES__[Field], short)

    @classmethod
    def trainings(cls, iterable, short=True):
        return cls.from_iterable(iterable, Training.name_fr,
                                 __ADDRESSES__[Training], short)

    @classmethod
    def skills(cls, iterable, short=False):
        return cls.from_iterable(iterable, Skill.name_fr,
                                 __ADDRESSES__[Skill], short)

    @classmethod
    def modules(cls, iterable, short=False):
        return cls.from_iterable(iterable, Module.name_fr,
                                 __ADDRESSES__[Module], short)

    @classmethod
    def criteria(cls, iterable, short=False):
        return cls.from_iterable(iterable, Criterion.name_fr,
                                 __ADDRESSES__[Criterion], short)

    @classmethod
    def fields_from_skills(cls, skills, short=True):
        d = {}
        for skill in skills:
            d.update({x.id: x for x in skill.get_fields()})
        return cls.fields(d.values(), short)

    @classmethod
    def trainings_from_modules(cls, modules, short=True):
        trainings = {m.training for m in modules}
        return cls.trainings(trainings, short)

    @classmethod
    def skills_from_fields(cls, fields, short=False):
        d = {}
        for field in fields:
            d.update({x.id: x for x in
                      Skill.objects.filter(fields=field.id).distinct()})
        return cls.skills(d.values(), short)

    @classmethod
    def skills_from_modules(cls, modules, short=False):
        d = {}
        for module in modules:
            d.update({x.id: x for x in module.get_skills()})
        return cls.skills(d.values(), short)

    @classmethod
    def skills_from_criteria(cls, criteria, short=False):
        d = {}
        for criterion in criteria:
            d.update({x.id: x for x in criterion.get_skills()})
        return cls.skills(d.values(), short)

    @classmethod
    def modules_from_trainings(cls, trainings, short=False):
        d = {}
        for training in trainings:
            d.update({x.id: x for x in
                      Module.objects.filter(training=training.id).distinct()})
        return cls.modules(d.values(), short)

    @classmethod
    def modules_from_skills(cls, skills, short=False):
        skill_ids = [skill.id for skill in skills]
        modules = Module.objects.filter(skills__in=skill_ids).distinct()
        return cls.modules(modules, short)

    @classmethod
    def criteria_from_skills(cls, skills, short=False):
        skill_ids = [skill.id for skill in skills]
        criteria = Criterion.objects.filter(skills__in=skill_ids).distinct()
        return cls.criteria(criteria, short)

    def get_ids(self):
        return [s.id for s in self.list]

    def __iter__(self):
        return iter(self.list)


def fields(request):
    field_stickers = []
    for field in MainCategory.get_fields():
        skill_category = Category.skills_from_fields([field])

        module_category = Category.modules_from_skills(skill_category)

        training_category = Category.trainings_from_modules(module_category)

        criterion_category = Category.criteria_from_skills(skill_category)

        field_stickers.append(Sticker(field.id, field.long_name,
                                      [skill_category, module_category,
                                       training_category, criterion_category]))

    view = MainCategory.from_(Field, field_stickers)
    return render(request, 'planforma/stickers.html/', {'view': view})


def trainings(request):
    training_stickers = []
    for training in MainCategory.get_trainings():
        module_category = Category.modules_from_trainings([training])

        skill_category = Category.skills_from_modules(module_category)

        criterion_category = Category.criteria_from_skills(skill_category)

        field_category = Category.fields_from_skills(skill_category)

        training_stickers.append(Sticker(training.id, training.name,
                                         [field_category, module_category,
                                          skill_category, criterion_category]))

    view = MainCategory.from_(Training, training_stickers)
    return render(request, 'planforma/stickers.html/', {'view': view})


def modules(request):
    module_stickers = []
    for module in MainCategory.get_modules():
        training_category = Category.trainings_from_modules([module])

        skill_category = Category.skills_from_modules([module])

        field_category = Category.fields_from_skills(skill_category)

        criterion_category = Category.criteria_from_skills(skill_category)

        module_stickers.append(Sticker(module.id, module.name,
                                       [training_category, field_category,
                                        skill_category, criterion_category]))

    view = MainCategory.from_(Module, module_stickers)
    return render(request, 'planforma/stickers.html/', {'view': view})


def skills(request):
    skill_stickers = []
    for skill in MainCategory.get_skills():
        field_category = Category.fields_from_skills([skill])

        module_category = Category.modules_from_skills([skill])

        training_category = Category.trainings_from_modules(module_category)

        # Advices

        criterion_category = Category.criteria_from_skills([skill])

        skill_stickers.append(Sticker(skill.id, skill.name,
                                      [field_category, training_category,
                                       module_category, criterion_category]))

    view = MainCategory.from_(Skill, skill_stickers)
    return render(request, 'planforma/stickers.html/', {'view': view})


def criteria(request):
    criterion_stickers = []
    for criterion in MainCategory.get_criteria():
        skill_category = Category.skills_from_criteria([criterion])

        field_category = Category.fields_from_skills(skill_category)

        module_category = Category.modules_from_skills(skill_category)

        training_category = Category.trainings_from_modules(module_category)

        criterion_stickers.append(Sticker(criterion.id, criterion.name,
                                          [field_category, training_category,
                                           module_category, skill_category]))
    view = MainCategory.from_(Criterion, criterion_stickers)
    return render(request, 'planforma/stickers.html/', {'view': view})



