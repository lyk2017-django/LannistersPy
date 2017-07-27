from django.contrib import admin
from payment.models import Product,UserCard, PrepaidCard, Vendor

#Product
#UserCard
#PrepaidCard
#Vendor

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = [
        "name",
        "brand",
        "price",
    ]
    search_fields = [
        "name",
        "brand",
        "price",
    ]
@admin.register(UserCard)
class UserCardAdmin (admin.ModelAdmin):
    list_display = [
        "card_number",
        "balance",
    ]
    search_fields = [
        "card_number",
        "balance",
    ]

@admin.register(PrepaidCard)
class PrepaidCardAdmin (admin.ModelAdmin):
    list_display = [
        "barcode",
        "value",
    ]
    search_fields = [
        "barcode",
        "value",
    ]

@admin.register(Vendor)
class VendorAdmin (admin.ModelAdmin):
    list_display = [
        "location",
        "products",
    ]
    search_fields = [
        "location",
        "products",
    ]


