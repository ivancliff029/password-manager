from django.shortcuts import render
from passwords.models import Passwords
from passwords.forms import ProductForm 

# Create your views here.
def password_dashboard(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    passwords = Passwords.objects.all()
    return render(request, 'dashboard/dashboard.html', {'form': form, 'passwords': passwords})