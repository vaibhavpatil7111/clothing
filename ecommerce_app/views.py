from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, Count
from .models import UserProfile, Product, Category, Order, OrderItem, CartItem
from .forms import UserRegistrationForm, UserProfileForm
from django.http import JsonResponse

def home(request):
    products = Product.objects.filter(is_active=True)[:8]
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Create admin user if doesn't exist
        if username == 'admin' and password == 'admin':
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@risearc.com', 'admin')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                profile = UserProfile.objects.get(user=user)
                if not profile.is_active:
                    messages.error(request, 'Your account is inactive. Please contact admin.')
                    return render(request, 'login.html')
            except UserProfile.DoesNotExist:
                pass
            
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if user already exists
            if User.objects.filter(username=email).exists():
                messages.error(request, 'User with this email already exists.')
                return render(request, 'register.html', {'form': form})
            
            try:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=form.cleaned_data['password']
                )
                
                UserProfile.objects.create(
                    user=user,
                    full_name=form.cleaned_data['full_name'],
                    address=form.cleaned_data['address'],
                    contact_number=form.cleaned_data['contact_number'],
                    date_of_birth=form.cleaned_data['date_of_birth'],
                    profile_photo=form.cleaned_data.get('profile_photo')
                )
                
                messages.success(request, 'Registration successful! Please login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def user_dashboard(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'user_dashboard.html', {
        'profile': profile,
        'orders': orders
    })

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    
    total_users = UserProfile.objects.count()
    active_users = UserProfile.objects.filter(is_active=True).count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    recent_orders = Order.objects.order_by('-created_at')[:10]
    users = UserProfile.objects.all().order_by('-created_at')
    
    return render(request, 'admin_dashboard.html', {
        'total_users': total_users,
        'active_users': active_users,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'recent_orders': recent_orders,
        'users': users
    })

@login_required
def toggle_user_status(request, user_id):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    
    profile = get_object_or_404(UserProfile, id=user_id)
    profile.is_active = not profile.is_active
    profile.save()
    
    messages.success(request, f'User status updated successfully.')
    return redirect('admin_dashboard')

@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_dashboard')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})

def products(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id, is_active=True)
    else:
        products = Product.objects.filter(is_active=True)
    
    categories = Category.objects.all()
    
    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if not request.session.session_key:
            request.session.create()
        
        cart_item, created = CartItem.objects.get_or_create(
            session_key=request.session.session_key,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        messages.success(request, f'{product.name} added to cart!')
        return redirect('product_detail', product_id=product_id)
    
    return redirect('products')

def view_cart(request):
    if not request.session.session_key:
        cart_items = []
    else:
        cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    
    total = sum(item.total_price for item in cart_items)
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, session_key=request.session.session_key)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('view_cart')

def user_logout(request):
    logout(request)
    return redirect('login')