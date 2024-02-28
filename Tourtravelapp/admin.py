from django.contrib import admin
from .models import Pakage,TourCart,Order
# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display = ['userid',
                     'pid', 
                     'pname',
                     'category',
                     'pprice', 
                     'pdescription', 
                     'pimage']
    

class TourCartAdmin(admin.ModelAdmin):
    list_display = ['userid',
                     'pid',
                     'qty']
                     
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['userid',
                     'pid',
                     'orderid',
                     'qty']

admin.site.register(Pakage,PackageAdmin)
admin.site.register(TourCart,TourCartAdmin)
admin.site.register(Order,OrderAdmin)