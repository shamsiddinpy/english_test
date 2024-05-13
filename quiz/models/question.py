from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE


class Question(Model):
    question = CharField(max_length=150)
    image = ImageField(upload_to='quiz/%Y/', blank=True)
    quiz = ForeignKey('Quiz', on_delete=CASCADE, verbose_name='test')

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = 'questions'
        verbose_name = 'savol'
        verbose_name_plural = 'savollar'
