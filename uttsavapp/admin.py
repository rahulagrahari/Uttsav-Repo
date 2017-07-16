# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import VendorListTable, VendorDetailTable, EventCategoryCT, VendingCategoryCT

# Register your models here.
admin.site.register(VendorListTable)
admin.site.register(VendorDetailTable)
admin.site.register(EventCategoryCT)
admin.site.register(VendingCategoryCT)
