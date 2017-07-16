# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class VendorListTable(models.Model):
    title = models.CharField(max_length=100)
    VendingCategory = models.IntegerField(default=None)
    EventCategory = models.IntegerField(default=None)

    # def get_absolute_url(self):
        #return reverse("post:detail", kwargs={"id": self.id})
        # return "/post/%s/" % self.id

    def __str__(self):
        return self.title


class VendorDetailTable(models.Model):

    vendorlisttable = models.ForeignKey(VendorListTable, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    vendor_desc = models.CharField(max_length=100)
    VendingCategory = models.IntegerField(default=None)
    EventCategory = models.IntegerField(default=None)
    vendor_email = models.EmailField()
    vendor_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.vendor_name


class VendorListToEventCategory(models.Model):
    vendorlistid = models.ForeignKey(VendorListTable, on_delete=models.CASCADE)
    EventCategory = models.IntegerField(default=None)


class VendorListToVendingCategory(models.Model):
    vendorlistid = models.ForeignKey(VendorListTable, on_delete=models.CASCADE)
    VendingCategory = models.IntegerField(default=None)


class VendorDetailToEventCategory(models.Model):
    vendordetailid = models.ForeignKey(VendorDetailTable, on_delete=models.CASCADE)
    EventCategory = models.IntegerField(default=None)


class VendorDetailToVendingCategory(models.Model):
    vendordetailid = models.ForeignKey(VendorDetailTable, on_delete=models.CASCADE)
    VendingCategory = models.IntegerField(default=None)


class EventCategoryCT(models.Model):

    event_name = models.CharField(max_length=50)
    event_code = models.IntegerField(default=None)


class VendingCategoryCT(models.Model):

    vending_name = models.CharField(max_length=50)
    vending_code = models.IntegerField(default=None)
