from django.db.models import Count
from django.shortcuts import render

from quiz.models import Category


def IndexView(request):
    categories = Category.objects.annotate(quiz_count=Count('quiz__id')).filter(quiz_count__gte=1).order_by('nnp')

    context = {
        'title': 'Bosh sahifa',
        'categories': categories,
    }
    return render(request, 'quiz/index.html', context=context)
