from django.contrib import admin
from .models import CustomUser, Client, Debt, Payment, Product, Purchase, ContactHistory, Fine, Notification, Checklist

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Debt)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(ContactHistory)
admin.site.register(Fine)
admin.site.register(Notification)
admin.site.register(Checklist)