from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
