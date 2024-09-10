from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'USB to Type C Cable',
        'price': 1000,
        'description': 'Multipurpose usb to type C cable',
        'stock': 1
    }

    return render(request, "main.html", context)