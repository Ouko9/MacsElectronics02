from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages
from .forms import ProductForm, ImageUploadForm
from .models import Member, Products, ImageModel


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('homepage')
        else:
            return HttpResponseRedirect(reverse('registration_failed'))
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product list')  # Redirect to a page displaying all products or a confirmation page
    else:
        form = ProductForm()

    return render(request, 'add_products.html', {'form': form})


def user_login(request):
    return render(request, 'user_login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def manage_products(request):
    return render(request, 'manage_products.html')


def add(request):
    return render(request, 'add_products.html')


def inner(request):
    return render(request, 'inner-page.html')


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Member.objects.filter(username=username, password=password).exists():
            member = Member.objects.get(username=username, password=password)
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')


def registration_failed(request):
    return render(request, 'registration_failed.html')



def payment_form(request):
    return render(request, 'payment_form.html')

def update_visibility(request, product_id):
    return render(request, 'update_visibility.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')

def show(request):
    return render(request, 'show.html')