from django.shortcuts import render
from core import models
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


@login_required
def products(request):
    product = models.product.objects.all()
    data = {'products':product}
    return render(request, 'products.html', data)


def base(request):
    return render(request, 'base.html')



def logout_view(request):
    logout(request)
    return products(request)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
