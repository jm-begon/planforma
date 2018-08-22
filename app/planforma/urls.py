from django.urls import path

from . import views
from . import models

urlpatterns = [
    path('', views.fields, name='index'),
    path(views.__ADDRESSES__[models.Field], views.fields, name='axes'),
    path(views.__ADDRESSES__[models.Training], views.trainings, name='formations'),
    path(views.__ADDRESSES__[models.Module], views.modules, name='modules'),
    path(views.__ADDRESSES__[models.Skill], views.skills, name='competences'),
    path(views.__ADDRESSES__[models.Criterion], views.criteria, name='criteres'),

]