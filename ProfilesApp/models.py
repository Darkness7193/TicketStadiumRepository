from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, ManyToManyField, CharField

from App1.models import Order


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    requisites = CharField(max_length=20)
    orders = ManyToManyField(Order, related_name='orders')

    def __str__(self):
        return self.requisites

    class Meta:
        db_table = 'profile'
