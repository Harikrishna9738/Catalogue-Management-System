from django.contrib import admin
from .models import Brand,Product,Category,Specifications
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('guest_name','govt_id','number_of_guest','age','contact','email')


admin.site.register(Guest,GuestAdmin)
