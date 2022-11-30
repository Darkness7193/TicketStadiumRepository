from django.db.models import (ForeignKey, Model, CharField, IntegerField, TimeField, DateField,
                              CASCADE, FloatField, SET_NULL, BooleanField)
from django.contrib.auth.models import User

from StadiumTickets.myShortcuts import MyManager


class Sector(Model):
    objects = MyManager()

    shortcut = IntegerField(null=True)
    price = IntegerField(null=True)

    def __str__(self):
        return str(self.shortcut)

    class Meta:
        db_table = 'sector'


class Stadium(Model):
    objects = MyManager()

    name = CharField(max_length=20)
    street = CharField(max_length=20)
    city = CharField(max_length=20)
    region = CharField(max_length=20)
    country = CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stadium'


class Match(Model):
    objects = MyManager()

    name = CharField(max_length=20)
    stadium = ForeignKey(Stadium, on_delete=CASCADE)
    side1 = CharField(max_length=20)
    side2 = CharField(max_length=20)
    coefficient = FloatField(default=1)
    date = DateField(null=True)
    time = TimeField(null=True)

    def __str__(self):
        return f'''
            {self.name} {self.side1} - {self.side2}
        '''

    class Meta:
        db_table = 'match'


class Place(Model):
    objects = MyManager()

    sector = ForeignKey(Sector, on_delete=SET_NULL, null=True)
    row = IntegerField()
    count = IntegerField()
    stadium = ForeignKey(Stadium, on_delete=CASCADE)

    def __str__(self):
        return f'{self.sector} сектор, {self.row} ряд, {self.count} место'

    class Meta:
        db_table = 'place'


class Ticket(Model):
    objects = MyManager()

    place = ForeignKey(Place, on_delete=CASCADE)
    match = ForeignKey(Match, on_delete=CASCADE)
    is_paid = BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ticket'
