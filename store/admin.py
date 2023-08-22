from django.contrib import admin
from .models import Customer, Product, Orders, Contactus, Feedback


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class ContactusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contactus, ContactusAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)