from django.contrib import admin
from catalog.models import Category, Product

# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'products_count')
    inlines = [ProductInline]
    search_fields = ['name']

    def products_count(self, obj):
        return obj.products.count()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
