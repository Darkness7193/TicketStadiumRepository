from django.db.models import (ForeignKey, Model, CharField, IntegerField, TimeField,
                              CASCADE, FloatField, SET_NULL, ManyToManyField, BooleanField,
                              DateField,)


class Stadium(Model):
    name = CharField(max_length=20)

    street = CharField(max_length=20)
    city = CharField(max_length=20)
    region = CharField(max_length=20)
    country = CharField(max_length=20, default="Russia")

    def __str__(self):
        return f'{self.region}, {self.city}, {self.street}: {self.name}'

    class Meta:
        db_table = 'stadium'


class Match(Model):
    name = CharField(max_length=20)
    stadium = ForeignKey(Stadium, on_delete=CASCADE)

    side1 = CharField(max_length=20)
    side2 = CharField(max_length=20)
    coefficient = FloatField(default=1)

    date = DateField(null=True)
    time = TimeField(null=True)

    def __str__(self):
        return f'''
            {self.name} {self.side1} - {self.side2}. {self.stadium.name}
            {self.date} {self.time}
        '''

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
        return f'''
            Сектор:{self.sector}, 
            ряд:{self.row}, 
            место:{self.count}
        '''

    class Meta:
        db_table = 'place'


class Order(Model):
    ticket = CharField(max_length=20, null=True)
    place = ForeignKey(Place, on_delete=CASCADE)
    match = ForeignKey(Match, on_delete=CASCADE)
    is_paid = BooleanField(default=False)

    def __str__(self):
        return str(self.place)

    class Meta:
        db_table = 'order'


class User(Model):
    requisites = CharField(max_length=20)
    number = CharField(max_length=10)
    email = CharField(max_length=20)
    orders = ManyToManyField(Order, related_name='orders')

    def __str__(self):
        return self.requisites

    class Meta:
        db_table = 'user'