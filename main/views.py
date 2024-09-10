from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'USB to Type C Cable',
        'price': 1000,
        'description': 'Multipurpose usb to type C cable',
        'stock': 1,
        'person_name': 'Edmond Christian',
        'npm': '2306208363',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)