from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LostFoundItemForm
from .models import LostFoundItem
from django.views.decorators.cache import cache_control



def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

# 🔐 Home view - requires login
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    return render(request, 'lostfound/home.html')


# 📝 Signup view - blocks logged-in users & auto-logins new users
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')  # If already logged in, redirect to home

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Auto-login after signup
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    
    return render(request, 'lostfound/signup.html')


# 🔐 Login view - blocks logged-in users from seeing login page again
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'lostfound/login.html')


# 🚪 Logout
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    return redirect('login')


# ➕ Add lost/found item
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_item(request):
    if request.method == 'POST':
        form = LostFoundItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.save()
            messages.success(request, 'Item reported successfully.')
            return redirect('item_list')
    else:
        form = LostFoundItemForm()
    return render(request, 'lostfound/add_item.html', {'form': form})


# 📋 View all items
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def item_list(request):
    items = LostFoundItem.objects.all().order_by('-date_reported')
    return render(request, 'lostfound/item_list.html', {'items': items})


# 🧢 View lost items only
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def lost_items(request):
    items = LostFoundItem.objects.filter(status='lost').order_by('-date_reported')
    return render(request, 'lostfound/lost_items.html', {'items': items})


# 🎒 View found items only
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def found_items(request):
    items = LostFoundItem.objects.filter(status='found').order_by('-date_reported')
    return render(request, 'lostfound/found_items.html', {'items': items})
