from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'nama barangnya',
        'price': 1000,
        'description': 'filler description',
        'stock': 0
    }

    return render(request, "main.html", context)