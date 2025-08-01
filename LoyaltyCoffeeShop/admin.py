from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Transaction)
admin.site.register(models.TransactionItem)
admin.site.register(models.LoyaltyPointLog)