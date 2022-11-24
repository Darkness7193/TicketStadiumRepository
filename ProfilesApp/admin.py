from django.contrib import admin
from . import models as m

modelRegister = admin.site.register


modelRegister(m.Profile)