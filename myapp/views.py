from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user =  get_object_or_404(User, username=username)
       
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page':page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')


    return render(request, 'login_register.html', {'form': form})

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else''  
    products = Product.objects.filter(
        Q(category__name__icontains=q) |
        Q(productname__icontains=q))
    categories = Category.objects.all()
    product_count = products.count
    context = {'products':products, 'categories':categories, 'product_count':product_count}
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, "product_detail.html", context)

def createProduct(request):
    form = ProductForm
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('category')
        category,created = Category.objects.get_or_create(name=category_name)
        
        Product.objects.create(
            category=category,
            productname=request.POST.get('productname'),
            quantity=request.POST.get('quantity'),
            description = request.POST.get('description')
        )
        
        return redirect('home')


    context={'form':form, 'categories':categories}
    return render(request, 'product_form.html', context)

def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    categories = Category.objects.all()
    form = UpdateForm(instance=product)
    
    if request.method =='POST':
        category_name = request.POST.get('category')
        category,created = Category.objects.get_or_create(name=category_name)
        
        product.productname = request.POST.get('productname')
        product.description = request.POST.get('description')
        product.category = category
        product.save()
        return redirect('home')

    context = {'form':form, 'categories':categories, 'product':product}
    return render(request, 'update_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method =='POST':
        product.delete()
        return redirect('home')
    
    context = {'obj':product}
    return render(request, 'delete.html ', context)

def deleteAllProducts(request):
    products = Product.objects.all()
    if request.method =='POST':
        products.delete()
        return redirect('home')
    
    context ={'products':products}
    return render(request, 'delete_all.html ')

def issue_items(request, pk):
    product = Product.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.receive_quantity = 0
        instance.quantity = (instance.quantity) - (instance.issue_quantity)
        instance.issue_by = str(request.user)
        instance.save()
        return redirect('home')

    context = {"product": product,"form": form}
    return render(request, "issue_items.html", context)

def receive_items(request, pk):
    product = Product.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_quantity = 0
        instance.receive_by = str(request.user)
        instance.quantity += instance.receive_quantity
        instance.save()
        return redirect('home')
		
    context = {"product": product,"form": form}
    return render(request, "receive_items.html", context)

@login_required
def list_history(request):
    history = ProductHistory.objects.all()
    form = ProductHistorySearchForm(request.POST or None)
    if request.method == 'POST':
        history = ProductHistory.objects.all()
    
    context = {"history": history,}
    return render(request, "history_list.html",context)