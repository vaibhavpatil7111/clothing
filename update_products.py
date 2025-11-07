#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clothing_ecommerce.settings')
django.setup()

from ecommerce_app.models import Category, Product

def update_products():
    """Update first 3 products with new items based on provided images"""
    
    # Get categories
    try:
        womens_category = Category.objects.get(name='Elite Womens Fashion')
    except Category.DoesNotExist:
        womens_category = Category.objects.create(
            name='Elite Womens Fashion',
            description='Luxury fashion for the contemporary woman'
        )
    
    # Delete first 3 products
    products_to_delete = Product.objects.all()[:3]
    for product in products_to_delete:
        product.delete()
        print(f'Deleted: {product.name}')
    
    # Create new products based on the images
    new_products = [
        {
            'name': 'Burgundy Ruffle Midi Dress',
            'description': 'Vintage-inspired burgundy dress with ruffled straps, fitted bodice, and tiered ruffle skirt with elegant side tie detail. Perfect for special occasions.',
            'category': womens_category,
            'price': 159.99,
            'stock': 25
        },
        {
            'name': 'Burgundy Casual Sweatsuit Set',
            'description': 'Comfortable burgundy sweatshirt and shorts set with stylish white stripe trim details. Perfect for casual wear and lounging.',
            'category': womens_category,
            'price': 89.99,
            'stock': 40
        },
        {
            'name': 'Forest Green Maxi Dress',
            'description': 'Elegant sleeveless forest green maxi dress with a fitted silhouette and flowing skirt. Sophisticated design for evening events.',
            'category': womens_category,
            'price': 179.99,
            'stock': 30
        }
    ]
    
    for product_data in new_products:
        product = Product.objects.create(**product_data)
        print(f'Created: {product.name} - ${product.price}')
    
    print('\nProducts updated successfully!')
    print('New products added based on your images.')

if __name__ == '__main__':
    update_products()