from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.


admin.site.register(Crypto)
admin.site.register(TradeIdea)
admin.site.register(Subscribe)