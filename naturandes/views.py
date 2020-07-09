from django.shortcuts import render, HttpResponse

# Create your views here.


def naturandes(request):
    """View that display the naturandes page"""
    return render(request, "naturandes.html")
