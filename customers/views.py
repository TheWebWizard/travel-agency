from django.shortcuts import render


def index(request):
    """ Display the customer's page"""

    if request.user.is_authenticated:

        template = 'customer/customer.html'
        context = {}

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
