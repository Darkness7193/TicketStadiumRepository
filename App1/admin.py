from django.contrib import admin
from . import models as m

modelRegister = admin.site.register


modelRegister(m.User)
modelRegister(m.Stadium)
modelRegister(m.Match)
modelRegister(m.Sector)
modelRegister(m.Place)
modelRegister(m.Ticket)

