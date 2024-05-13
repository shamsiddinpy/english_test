from django.db.models import Model, CharField, PositiveSmallIntegerField, SlugField, TextField
from django.urls import reverse


class Category(Model):
    title = CharField(max_length=150)
    description = TextField(blank=True)
    slug = SlugField(unique=True)
    nnp = PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'category'
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'category_slug': self.slug,
            }
        )
