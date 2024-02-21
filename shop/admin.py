from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Product, Category, Colour, Size


class ProductCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class ProductAdmin(admin.ModelAdmin):
    exclude = ('id',)


admin.site.register(Category, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Colour)
admin.site.register(Size)
