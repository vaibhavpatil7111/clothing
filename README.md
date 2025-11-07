# RiseArc - Premium Fashion E-Commerce Website

A complete Django-based e-commerce web application for RiseArc premium fashion brand with separate admin and user panels, featuring modern animations and responsive design.

## 🚀 Features

### User Features
- User registration with complete profile information
- Secure login/logout with authentication
- Interactive user dashboard with profile management
- Premium product browsing with animations
- Profile photo upload functionality
- Order history tracking

### Admin Features
- Comprehensive admin dashboard with business analytics
- User management (activate/deactivate accounts)
- Product management through Django admin
- Real-time revenue tracking
- User status control and monitoring

### Design Features
- **Modern UI/UX** with Bootstrap 5
- **Smooth animations** using Animate.css
- **Premium gradient designs** and hover effects
- **Responsive design** for all devices
- **RiseArc branding** throughout the application

## 🔐 Login Credentials

### Admin Access
**Username:** `admin`  
**Password:** `admin`

**Access Points:**
- Django Admin Panel: `http://127.0.0.1:8000/admin/`
- RiseArc Admin Dashboard: `http://127.0.0.1:8000/login/` (login with admin credentials)

### User Registration
- New users can register at: `http://127.0.0.1:8000/register/`
- Fill in all required fields including profile photo (optional)
- After registration, login at: `http://127.0.0.1:8000/login/`

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
cd clothing_ecommerce
pip install -r requirements.txt
```

### Step 2: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Sample Data & Admin
```bash
python manage.py shell -c "
from ecommerce_app.models import Category, Product
from django.contrib.auth.models import User

# Create admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@risearc.com', 'admin')
    print('Admin user created: username=admin, password=admin')

# Create categories
if not Category.objects.exists():
    categories = [
        ('Premium Men\'s Collection', 'Sophisticated clothing for the modern gentleman'),
        ('Elite Women\'s Fashion', 'Luxury fashion for the contemporary woman'),
        ('Signature Accessories', 'Premium accessories that complete your look'),
        ('Designer Footwear', 'Handcrafted shoes for every occasion')
    ]
    for name, desc in categories:
        Category.objects.create(name=name, description=desc)
    print('RiseArc categories created')

# Create sample products
if not Product.objects.exists():
    cat1 = Category.objects.get(name='Premium Men\'s Collection')
    cat2 = Category.objects.get(name='Elite Women\'s Fashion')
    cat3 = Category.objects.get(name='Signature Accessories')
    
    products = [
        ('RiseArc Signature Polo', 'Premium cotton polo shirt with signature RiseArc emblem', cat1, 89.99, 50),
        ('Executive Blazer', 'Tailored blazer for the modern professional', cat1, 299.99, 25),
        ('Elegance Dress', 'Sophisticated evening dress for special occasions', cat2, 199.99, 30),
        ('Power Suit Jacket', 'Empowering blazer for the confident woman', cat2, 249.99, 20),
        ('RiseArc Luxury Watch', 'Premium timepiece with RiseArc craftsmanship', cat3, 599.99, 15),
        ('Designer Handbag', 'Handcrafted leather bag with premium finish', cat3, 399.99, 25),
        ('Comfort Chinos', 'Premium comfort chinos for everyday elegance', cat1, 129.99, 40),
        ('Silk Scarf Collection', 'Luxurious silk scarves in various designs', cat2, 79.99, 35)
    ]
    
    for name, desc, category, price, stock in products:
        Product.objects.create(
            name=name,
            description=desc,
            category=category,
            price=price,
            stock=stock
        )
    print('RiseArc premium products created')
"
```

### Step 4: Run the Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 🎯 Usage Guide

### For Administrators
1. **Django Admin Panel:** `http://127.0.0.1:8000/admin/`
   - Username: `admin`, Password: `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         `
   - Manage products, categories, users, and orders
   - Full CRUD operations on all models

2. **RiseArc Admin Dashboard:** `http://127.0.0.1:8000/login/`
   - Login with admin credentials
   - View business statistics and analytics
   - Manage user accounts (activate/deactivate)
   - Monitor recent orders and revenue

### For Users
1. **Registration:** `http://127.0.0.1:8000/register/`
   - Create new account with profile information
   - Upload profile photo (optional)
   - Automatic account activation

2. **User Dashboard:** `http://127.0.0.1:8000/login/`
   - View and edit profile information
   - Check account status
   - View order history
   - Browse premium products

## 🌐 Key URLs

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | RiseArc homepage with featured products |
| **Login** | `/login/` | User/Admin login page |
| **Register** | `/register/` | New user registration |
| **User Dashboard** | `/dashboard/` | User profile and order history |
| **Admin Dashboard** | `/admin-dashboard/` | Admin analytics and user management |
| **Products** | `/products/` | Premium product catalog |
| **Product Detail** | `/product/<id>/` | Individual product information |
| **Django Admin** | `/admin/` | Full admin panel (admin/admin) |

## 📦 Sample Products Included

The setup script creates these premium RiseArc products:

### Premium Men's Collection
- **RiseArc Signature Polo** - $89.99
- **Executive Blazer** - $299.99
- **Comfort Chinos** - $129.99

### Elite Women's Fashion
- **Elegance Dress** - $199.99
- **Power Suit Jacket** - $249.99
- **Silk Scarf Collection** - $79.99

### Signature Accessories
- **RiseArc Luxury Watch** - $599.99
- **Designer Handbag** - $399.99

All products include stock quantities and detailed descriptions.

## 🎨 Design Features

### Modern UI/UX
- **Responsive Bootstrap 5 design**
- **Animate.css animations** for smooth interactions
- **Google Fonts (Poppins)** for modern typography
- **Gradient backgrounds** and hover effects
- **Premium color scheme** with RiseArc branding

### Interactive Elements
- **Floating animations** on product cards
- **Pulse effects** on buttons
- **Smooth transitions** and hover states
- **Animated counters** on admin dashboard
- **Progressive image loading** with fallback images

## 🔧 Troubleshooting

### Common Issues

1. **Registration Error (UNIQUE constraint failed)**
   - This happens when trying to register with an existing email
   - Use a different email address or check if account already exists

2. **Admin login not working**
   - Ensure you're using: Username: `admin`, Password: `admin`
   - If admin doesn't exist, it will be created automatically on first login attempt

3. **Media files not loading**
   ```bash
   # Create media directory
   mkdir media
   mkdir media/profile_photos
   mkdir media/products
   ```

4. **Database errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **No products showing**
   - Run the sample data creation script from Step 3 above
   - Or add products manually through Django admin panel

### Reset Database (if needed)
```bash
# Delete database and start fresh
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
# Then run the sample data script again
```

## 📞 Support

**Default Login Credentials:**
- **Admin:** username=`admin`, password=`admin`
- **Django Admin:** Same credentials as above
- **New Users:** Register at `/register/` with any valid email

**Quick Test Account Creation:**
```python
# Run in Django shell: python manage.py shell
from django.contrib.auth.models import User
from ecommerce_app.models import UserProfile

# Create test user
user = User.objects.create_user('test@risearc.com', 'test@risearc.com', 'test123')
UserProfile.objects.create(
    user=user,
    full_name='Test User',
    address='123 Test Street',
    contact_number='1234567890',
    date_of_birth='1990-01-01'
)
```

## 🚀 Future Enhancements

### Phase 1 - E-commerce Core
- **Shopping Cart** with session management
- **Checkout Process** with order confirmation
- **Payment Integration** (Stripe/PayPal)
- **Order Status Tracking** for users

### Phase 2 - Advanced Features
- **Email Notifications** for orders and updates
- **Product Reviews & Ratings** system
- **Wishlist Functionality** for users
- **Advanced Search & Filters**

### Phase 3 - Business Intelligence
- **Advanced Analytics Dashboard**
- **Inventory Management** with low stock alerts
- **Sales Reports** and trend analysis
- **Customer Segmentation** and insights

## 📁 Project Structure

```
clothing_ecommerce/
├── manage.py
├── requirements.txt
├── README.md
├── clothing_ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── ecommerce_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── user_dashboard.html
│   │   ├── admin_dashboard.html
│   │   ├── edit_profile.html
│   │   ├── products.html
│   │   └── product_detail.html
│   └── static/
│       └── css/
│           └── style.css
├── media/ (created automatically)
└── db.sqlite3 (created after migration)
```

---

**© 2024 RiseArc - Rise Above Fashion**  
*Elevating Fashion, Empowering Style*