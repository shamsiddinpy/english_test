from django.db.models import Model, ForeignKey, CharField, SlugField, PROTECT, TextField, BooleanField, DateTimeField, \
    PositiveSmallIntegerField
from django.urls import reverse

from apps.model import Account
from quiz.models.categories import Category


class Quiz(Model):
    title = CharField(max_length=200)
    slug = SlugField('URL', unique=True)
    author = ForeignKey(Account, on_delete=PROTECT, verbose_name='avtar')
    description = TextField(blank=True)
    is_public = BooleanField(default=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
    category = ForeignKey(Category, on_delete=PROTECT)
    nnp = PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Quiz'
        verbose_name = 'Test'
        verbose_name_plural = 'Testlar'

        unique_together = (
            'slug',
            'category',
        )

    def get_absolute_url(self):
        return reverse(
            'quiz',
            kwargs={
                'quiz_slug': self.slug,
                'category_slug': self.category.slug,

            }
        )
