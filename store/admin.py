from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.
admin.site.site_header = "Sundar Adminstration"
admin.site.site_title = "Sundar Cement"
admin.site.index_title = "Welcome to this portal"


class ProductAdmin(admin.ModelAdmin):
#    exclude = ('pub_date',)
   sortable_by = 'id'
   list_display =  ('name', 'code', 'short_description', 'description', 'details', 'is_featured', 'is_active', 'category')
   list_display_links = ('name', 'code')
   list_filter = ['name', 'pub_date']
   ordering = ['name']

class SettingAdmin(admin.ModelAdmin):
    list_display =  ('name', 'email', 'phone', 'location')
    list_display_links = ('name', 'email')
    list_filter = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display =  ('name', 'code', 'pub_date')
    list_display_links = ('name', 'code')
    list_filter = ['name']
    
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Contact)
admin.site.register(Product,ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(BannerImage)
admin.site.register(Brochure)