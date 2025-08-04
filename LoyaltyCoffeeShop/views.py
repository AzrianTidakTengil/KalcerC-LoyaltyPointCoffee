from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from . import models
import re

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if username and email and password and confirm_password:
            if password != confirm_password:
                return HttpResponse("Passwords do not match.")
            
            if models.Customer.objects.filter(email=email).exists():
                return HttpResponse("Email already registered.")
            
            if len(password) < 8:
                return HttpResponse("Password must be at least 8 characters long.")
            
            if not re.match(r'^[a-zA-Z0-9]+$', username):
                return HttpResponse("Username must be alphanumeric.")
            
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return HttpResponse("Invalid email format.")

            customer = models.Customer(name=username, email=email, password=password)
            customer.save()

            request.session['user'] = {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email
            }

            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Please fill all fields.")
    return render(request, 'auth/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            customer = models.Customer.objects.get(email=email, password=password)
            request.session['user'] = {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email
            }
            return HttpResponseRedirect('/')
        except models.Customer.DoesNotExist:
            return HttpResponse("Invalid email or password.")
    return render(request, 'auth/login.html')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/auth/login')

def menu(request):
    products = models.Product.objects.all()
    user = request.session.get('user', None)
    return render(request, 'customer/menu.html', {'products': products, 'user': user})

def checkout(request):
    if request.method == 'POST':
        order_details = json.loads(request.body.decode('utf-8')).get('order_details', [])
        products = models.Product.objects.all()

        if not order_details:
            return JsonResponse({"message": "No items in the order.", "status": "error"}, status=400)

        transaction = models.Transaction.objects.create(customer_id=1)

        models.TransactionItem.objects.bulk_create([
            models.TransactionItem(
                transaction=transaction,
                product_id=int(item['id']),
                quantity=int(item['qty'])
            ) for item in order_details
        ])

    return JsonResponse({"message": "Order placed successfully!", "status": "success", "order_id": transaction.id}, status=200)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    customer_id = request.session.get('user', {}).get('id')
    try:
        customer = models.Customer.objects.get(id=customer_id)
        return render(request, 'customer/profile.html', {'customer': customer})
    except models.Customer.DoesNotExist:
        return HttpResponse("Customer not found.")

def order_detail(request, order_id):
    try:
        order = models.Transaction.objects.get(id=order_id)

        items = models.TransactionItem.objects.filter(transaction=order)
        order_items = []
        for item in items:
            product = item.product
            order_items.append({
                'product_name': product.name,
                'quantity': item.quantity,
                'price': product.price,
                'total': product.price * item.quantity
            })

        order.subtotal = sum(item['total'] for item in order_items)
        order.tax = int(order.subtotal * 0.15)
        order.total_amount = int(order.subtotal + order.tax)
    except models.Transaction.DoesNotExist:
        return HttpResponse("Order not found.")

    return render(request, 'customer/order_detail.html', {'order': order})

def order_history(request):
    return render(request, 'order_history.html')

def order(request):
    return render(request, 'order.html')

def cancel_order(request, order_id):
    return render(request, 'cancel_order.html', {'order_id': order_id})

def add_order(request):
    return render(request, 'add_order.html')

def update_order(request, order_id):
    return render(request, 'update_order.html', {'order_id': order_id})

def loyalty_program(request):
    return render(request, 'loyalty_program.html')

def add_menu_item(request):
    return render(request, 'add_menu_item.html')

def update_menu_item(request, item_id):
    return render(request, 'update_menu_item.html', {'item_id': item_id})

def delete_menu_item(request, item_id):
    return render(request, 'delete_menu_item.html', {'item_id': item_id})

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        
        try:
            customer = models.Customer.objects.get(email=email)
            customer.password = new_password
            customer.save()
            return HttpResponse("Password reset successful!")
        except models.Customer.DoesNotExist:
            return HttpResponse("Email not found.")
    return render(request, 'auth/reset_password.html')