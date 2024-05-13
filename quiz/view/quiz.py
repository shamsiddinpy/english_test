from django.utils.safestring import SafeString
from django.shortcuts import render, get_object_or_404
from quiz.models import Quiz


def QuizView(request, category_slug, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug, category__slug=category_slug)
    questions = quiz.question_set.all()

    quiz_data = {
        'questions': []
    }

    for question in questions:
        question_data = {
            'q': question.question,
            'a': '',
            'options': [],
        }

        for answer in question.answer_set.all():
            if answer.is_correct:
                question_data['a'] = answer.answer
            question_data['options'].append(answer.answer)

        quiz_data['questions'].append(question_data)

    context = {
        'title': quiz.title,
        'quiz_data': SafeString(quiz_data),
    }

    return render(request, 'quiz/quiz.html', context=context)
