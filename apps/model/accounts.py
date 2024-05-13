from django.contrib.auth.models import User
from django.db.models import Model, CharField, BooleanField, OneToOneField, CASCADE


class Account(Model):
    login = OneToOneField(User, verbose_name='login', null=True, blank=True, on_delete=CASCADE)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    can_create = BooleanField(default=True)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'account'
        verbose_name_plural = 'accounty'

    def __str__(self):
        username = f'({self.login.username})' if self.login else ''
        return self.first_name + ' ' + self.last_name
