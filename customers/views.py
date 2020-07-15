from django.shortcuts import render


def customer(request):
    """ Display the customer's page"""

    template = 'customer/customer.html'
    context = {}

    return render(request, template, context)
