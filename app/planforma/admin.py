from django.contrib import admin

from planforma.forms import AdviceForm
from .models import Field, Skill, Module, Criterion


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'fields', 'advices']
    form = AdviceForm


admin.site.register(Field)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Module)
admin.site.register(Criterion)


