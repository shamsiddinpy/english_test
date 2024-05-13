from django.contrib import admin

from quiz.admin.asiwer import AnswerTabularInline
from quiz.models import Question


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    inlines = (
        AnswerTabularInline,
    )
