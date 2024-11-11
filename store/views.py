from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Client, Product, Order
from .forms import ClientForm, OrderForm, ProductForm
from django.utils import timezone
from django.utils.timezone import now, timedelta
from django.db.models import Q

import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'store/home.html')

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    return render(request, 'store/add_client.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'store/create_product.html', {'form': form})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'store/add_order.html', {'form': form})

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    now = timezone.now()
    seven_days_ago = now - timedelta(days=7)
    thirty_days_ago = now - timedelta(days=30)
    year_ago = now - timedelta(days=365)

    last_7_days_orders = Order.objects.filter(client=client, ordered_at__gte=seven_days_ago)
    last_30_days_orders = Order.objects.filter(client=client, ordered_at__gte=thirty_days_ago)
    last_365_days_orders = Order.objects.filter(client=client, ordered_at__gte=year_ago)

    return render(request, 'store/client_orders.html', {
        'client': client,
        'last_7_days_orders': last_7_days_orders,
        'last_30_days_orders': last_30_days_orders,
        'last_365_days_orders': last_365_days_orders
    })

def about(request):
    return render(request, 'store/about.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'store/client_list.html', {'clients': clients})
