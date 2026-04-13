from django.contrib import admin
from .models import Category, Product, Order, OrderItem, NewsletterSubscriber, ProductImage


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(NewsletterSubscriber)
admin.site.register(ProductImage)