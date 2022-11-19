from django.contrib import admin
from . import models as m

modelRegister = admin.site.register


modelRegister(m.Stadium)
modelRegister(m.Match)
modelRegister(m.Sector)
modelRegister(m.Place)
modelRegister(m.Order)
modelRegister(m.User)
