from django.contrib import admin

from quiz.models import Question
from quiz.models.quiz import Quiz


@admin.register(Quiz)
class QuizModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }



