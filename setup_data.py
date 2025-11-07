#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clothing_ecommerce.settings')
django.setup()

from django.contrib.auth.models import User
from ecommerce_app.models import Category, Product

def setup_admin():
    """Create or update admin user"""
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('admin')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print('Admin updated: username=admin, password=admin')
    except User.DoesNotExist:
        User.objects.create_superuser('admin', 'admin@risearc.com', 'admin')
        print('Admin created: username=admin, password=admin')

def setup_categories():
    """Create product categories"""
    categories_data = [
        ('Premium Mens Collection', 'Sophisticated clothing for the modern gentleman'),
        ('Elite Womens Fashion', 'Luxury fashion for the contemporary woman'),
        ('Signature Accessories', 'Premium accessories that complete your look'),
        ('Designer Footwear', 'Handcrafted shoes for every occasion')
    ]
    
    for name, description in categories_data:
        category, created = Category.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            print(f'Created category: {name}')
        else:
            print(f'Category exists: {name}')

def setup_products():
    """Create sample products with images"""
    # Clear existing products
    Product.objects.all().delete()
    print('Cleared existing products')
    
    # Get categories
    cat1 = Category.objects.get(name='Premium Mens Collection')
    cat2 = Category.objects.get(name='Elite Womens Fashion')
    cat3 = Category.objects.get(name='Signature Accessories')
    cat4 = Category.objects.get(name='Designer Footwear')
    
    products_data = [
        {
            'name': 'RiseArc Signature Polo',
            'description': 'Premium cotton polo shirt with signature RiseArc emblem. Crafted from the finest materials for ultimate comfort and style.',
            'category': cat1,
            'price': 89.99,
            'stock': 50
        },
        {
            'name': 'Executive Blazer',
            'description': 'Tailored blazer for the modern professional. Perfect fit and premium fabric for business excellence.',
            'category': cat1,
            'price': 299.99,
            'stock': 25
        },
        {
            'name': 'Comfort Chinos',
            'description': 'Premium comfort chinos for everyday elegance. Versatile and stylish for any occasion.',
            'category': cat1,
            'price': 129.99,
            'stock': 40
        },
        {
            'name': 'Classic Denim Jeans',
            'description': 'Premium quality denim jeans with perfect fit. Timeless style meets modern comfort.',
            'category': cat1,
            'price': 149.99,
            'stock': 35
        },
        {
            'name': 'Elegance Dress',
            'description': 'Sophisticated evening dress for special occasions. Designed to make you feel confident and beautiful.',
            'category': cat2,
            'price': 199.99,
            'stock': 30
        },
        {
            'name': 'Power Suit Jacket',
            'description': 'Empowering blazer for the confident woman. Professional elegance meets modern style.',
            'category': cat2,
            'price': 249.99,
            'stock': 20
        },
        {
            'name': 'Silk Scarf Collection',
            'description': 'Luxurious silk scarves in various designs. The perfect accessory for any outfit.',
            'category': cat2,
            'price': 79.99,
            'stock': 35
        },
        {
            'name': 'Designer Blouse',
            'description': 'Elegant blouse perfect for office wear. Sophisticated design with premium fabric.',
            'category': cat2,
            'price': 119.99,
            'stock': 28
        },
        {
            'name': 'RiseArc Luxury Watch',
            'description': 'Premium timepiece with RiseArc craftsmanship. Precision meets elegance in every detail.',
            'category': cat3,
            'price': 599.99,
            'stock': 15
        },
        {
            'name': 'Designer Handbag',
            'description': 'Handcrafted leather bag with premium finish. Luxury and functionality in perfect harmony.',
            'category': cat3,
            'price': 399.99,
            'stock': 25
        },
        {
            'name': 'Premium Wallet',
            'description': 'Genuine leather wallet with RFID protection. Style and security combined.',
            'category': cat3,
            'price': 89.99,
            'stock': 40
        },
        {
            'name': 'Signature Sunglasses',
            'description': 'Designer sunglasses with UV protection. Fashion meets functionality.',
            'category': cat3,
            'price': 159.99,
            'stock': 30
        },
        {
            'name': 'Premium Sneakers',
            'description': 'Comfortable and stylish sneakers for everyday wear. Premium materials and modern design.',
            'category': cat4,
            'price': 179.99,
            'stock': 45
        },
        {
            'name': 'Leather Oxford Shoes',
            'description': 'Classic leather oxford shoes for formal occasions. Timeless elegance and superior craftsmanship.',
            'category': cat4,
            'price': 259.99,
            'stock': 30
        },
        {
            'name': 'Casual Loafers',
            'description': 'Comfortable loafers for casual and semi-formal occasions. Perfect blend of style and comfort.',
            'category': cat4,
            'price': 199.99,
            'stock': 35
        },
        {
            'name': 'Athletic Running Shoes',
            'description': 'High-performance running shoes with advanced cushioning. Built for comfort and durability.',
            'category': cat4,
            'price': 149.99,
            'stock': 50
        }
    ]
    
    for product_data in products_data:
        product = Product.objects.create(**product_data)
        print(f'Created product: {product.name} - ${product.price}')

def main():
    print('Setting up RiseArc E-commerce Data...\n')
    
    setup_admin()
    print()
    
    setup_categories()
    print()
    
    setup_products()
    print()
    
    print('Setup Complete!')
    print('=' * 50)
    print('LOGIN CREDENTIALS:')
    print('   Username: admin')
    print('   Password: admin')
    print()
    print('ACCESS POINTS:')
    print('   Website: http://127.0.0.1:8000/')
    print('   Django Admin: http://127.0.0.1:8000/admin/')
    print('   Admin Dashboard: http://127.0.0.1:8000/login/')
    print('=' * 50)

if __name__ == '__main__':
    main()