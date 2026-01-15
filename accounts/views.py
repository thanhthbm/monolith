from django.shortcuts import render, redirect

from accounts.models import Customer


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        Customer.objects.create(name=name, email=email, password=password)
        return redirect('login')
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        customer = Customer.objects.filter(
            email=email,
            password=password
        ).first()

        if customer:
            request.session['customer_id'] = customer.id
            return redirect('book_list')

    return render(request, 'accounts/login.html')

def logout(request):
    request.session.clear()
    return redirect('login')