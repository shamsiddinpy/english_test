from django.contrib import admin
from django.contrib.admin import TabularInline

from quiz.models import Answer


class AnswerTabularInline(TabularInline):
    model = Answer
    min_mun = 2
    extra = 0
