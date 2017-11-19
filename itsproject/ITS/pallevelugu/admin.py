# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Members,Farms,Wells,Crop,Vill,Dealer,Medicare,MediUpdates
#admin.site.register(Households)
admin.site.register(Members)
admin.site.register(Farms)
admin.site.register(Wells)
admin.site.register(Crop)
admin.site.register(Vill)
admin.site.register(Dealer)
admin.site.register(Medicare)
admin.site.register(MediUpdates)



