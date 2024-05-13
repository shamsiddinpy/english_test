from django.db.models import Model, CharField, BooleanField, ForeignKey, CASCADE

from quiz.models import Question


class Answer(Model):
    answer = CharField(max_length=150)
    is_correct = BooleanField(default=False)
    comment = CharField(
        max_length=100,
        blank=True
    )
    question = ForeignKey(Question, on_delete=CASCADE, verbose_name='question')

    class Meta:
        db_table = 'answers'
        verbose_name = 'javob'
        verbose_name_plural = 'javoblar'
