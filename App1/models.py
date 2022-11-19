from django.db.models import (ForeignKey, Model, CharField, IntegerField, TimeField,
                              CASCADE, FloatField, SET_NULL, ManyToManyField)


class Stadium(Model):
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
    name = CharField(max_length=20)
    stadium = ForeignKey(Stadium, on_delete=CASCADE)

    side1 = CharField(max_length=20)
    side2 = CharField(max_length=20)
    coefficient = FloatField(default=1)

    year = IntegerField(null=True)
    day = IntegerField(null=True)
    time = TimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'match'


class Sector(Model):
    name = CharField(max_length=20)
    price = IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sector'


class Place(Model):
    sector = ForeignKey(Sector, on_delete=SET_NULL, null=True)
    row = IntegerField()
    count = IntegerField()
    stadium = ForeignKey(Stadium, on_delete=CASCADE)

    def __str__(self):
        return str(self.row)

    class Meta:
        db_table = 'place'


class Order(Model):
    ticket = CharField(max_length=1)
    place = ForeignKey(Place, on_delete=CASCADE)
    match = ForeignKey(Match, on_delete=CASCADE)

    def __str__(self):
        return str(self.place) + str(self.match)

    class Meta:
        db_table = 'order'


class User(Model):
    requisites = CharField(max_length=20)
    number = CharField(max_length=10)
    email = CharField(max_length=20)
    unpaid_orders = ManyToManyField(Order, related_name="unpaid_orders")
    paid_orders = ManyToManyField(Order, related_name="paid_orders")

    def __str__(self):
        return self.requisites

    class Meta:
        db_table = 'user'