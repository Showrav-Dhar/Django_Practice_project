from django.contrib import admin
from products.models import Product,offers
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stocks')

class offersAdmin(admin.ModelAdmin):
    list_display = ('offer_code','discount')



admin.site.register(Product,ProductAdmin)
admin.site.register(offers,offersAdmin)
