from django.shortcuts import render, redirect, reverse
from main.forms import NewProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'username': request.user.username,
        'name' : 'Edmond Christian',
        'price': 1000,
        'description': 'Multipurpose usb to type C cable',
        'stock': 1,
        'person_name': 'Edmond Christian',
        'npm': '2306208363',
        'class': 'PBP D',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def add_product(request):
    form = NewProductForm(request.POST, request.FILES or None)

    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('main:show_main')
    else:
        form = NewProductForm()
    
    context = {'form': form}
    return render(request, "add_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            messages.info(request, 'Account registration failed')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Dapatkan objek product yang ingin diedit
    product = Product.objects.get(pk = id)

    form = NewProductForm(request.POST or None, instance = product)

    if form.is_valid() and request.method == "POST":
        form = NewProductForm(request.POST, request.FILES, instance = product)
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
