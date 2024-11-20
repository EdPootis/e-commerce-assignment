from django.shortcuts import render, redirect, reverse
from main.forms import NewProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
import datetime, json, uuid, requests, io, tempfile
from PIL import Image

@login_required(login_url='/login')
def show_main(request):
    # products = Product.objects.filter(user=request.user)

    context = {
        'username': request.user.username,
        'name' : 'Edmond Christian',
        'price': 1000,
        'description': 'Multipurpose usb to type C cable',
        'stock': 1,
        'person_name': 'Edmond Christian',
        'npm': '2306208363',
        'class': 'PBP D',
        # 'products': products,
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
    # data = Product.objects.all()
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def show_json(request):
    # data = Product.objects.all()
    data = Product.objects.filter(user=request.user)
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
            messages.error(request, "Invalid username or password. Please try again.")

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

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    image = request.FILES.get("image")
    user = request.user
    
    if (not (name == "" or description == "")):
        new_product = Product(name=name, price=price, description=description, stock=stock, image=image, user=user)
        new_product.save()

    return HttpResponse(b"CREATED", status=201) 

@csrf_exempt
def add_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        image_url = data['image']

        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check if the request was successful
            with tempfile.NamedTemporaryFile(delete=False) as img_temp:
                img_temp.write(response.content)
                img_temp.flush()
                img_temp.seek(0)
                img = Image.open(io.BytesIO(response.content))
                img_format = img.format.lower()
                if img_format not in ['jpeg', 'png', 'gif', 'bmp']:
                    return JsonResponse({"status": "error", "message": "Invalid image format"}, status=400)

                new_product = Product.objects.create(
                    user=request.user,
                    name=data['name'],
                    price=int(data['price']),
                    description=data['description'],
                    stock=int(data['stock']),
                )
                
                new_product.image.save(f"{uuid.uuid4()}.{img_format}", ContentFile(img_temp.read()), save=True)
            
            return JsonResponse({"status": "success"}, status=200)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"status": "error", "message": "Invalid URL"}, status=400)
        except IOError:
            return JsonResponse({"status": "error", "message": "Invalid image content"}, status=400)
    else:
        return JsonResponse({"status": "error"}, status=401)