from django.contrib import admin
from .models import UserProfile, Category, Product, Order, OrderItem, CartItem

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'contact_number', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['full_name', 'user__username', 'user__email']
    list_editable = ['is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock', 'is_active']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'user__email']
    list_editable = ['status']
    inlines = [OrderItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'session_key', 'created_at']
    list_filter = ['created_at']
    search_fields = ['product__name']