from django.shortcuts import get_object_or_404, render
from quiz.models import Category, Quiz


def CategoryView(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    quizs = Quiz.objects.filter(category=category, is_public=True).order_by('title')

    context = {
        'title': f'Mavzu boyicha testlar «{category.title}»',
        'category': category,
        'quizs': quizs,
    }

    return render(request, 'quiz/categories.html', context=context)
