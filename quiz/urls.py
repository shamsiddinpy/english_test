from django.urls import path

from quiz.view import IndexView, CategoryView, QuizView

urlpatterns = [
    path('', IndexView, name='index'),
    path('<slug:category_slug>', CategoryView, name='category'),
    path('<slug:category_slug>/<slug:quiz_slug>', QuizView, name='quiz'),

]
