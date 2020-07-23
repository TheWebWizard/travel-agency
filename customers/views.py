from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Customer


def index(request):
    """ Display the customer's page"""

    if request.user.is_authenticated:
        # user is indentified by his email
        # user = User.objects.get(email=request.user.email)

        profile = get_object_or_404(Customer, user=request.user)

        if request.user == 'hoii':
            template = 'customer/customer.html'
            context = {
                'profile': profile,
            }
        else:
            template = 'customer/customer1.html'
            context = {
                'profile': profile,
            }

        return render(request, template, context)

    else:
        template = 'allauth/account/login.html'
        context = {}

        return render(request, template, context)


def customer(request):
    """ Display the customer's page"""

    template = 'customer/customer.html'
    context = {}

    return render(request, template, context)


def logout(request):
    """Link to logout page"""

    template = 'allauth/account/logout.html'
    context = {}

    return render(request, template, context)

def signup(request):
    """Link to logout page"""

    template = 'allauth/account/signup.html'
    context = {}

    return render(request, template, context)
