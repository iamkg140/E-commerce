from typing import ContextManager
from django.shortcuts import redirect, render
from store.models import Contact, Product, Category, Setting, BannerImage, Brochure, OrderItem
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def home(request):
    category_list = Category.objects.all().order_by('-id')[:4]
    product_list = Product.objects.all().order_by('-id')
    featured_list = Product.objects.filter(is_featured = True, is_active = True)[:5]
    setting = Setting.objects.first()
    banner_image = BannerImage.objects.all()
    context = {'category_list' : category_list, 'product_list' : product_list, 'featured_list': featured_list,'setting': setting, 'banner_image': banner_image}
    return render(request, 'store/index.html', context)

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            message = message
        )
        return HttpResponse('')
    category_list = Category.objects.all().order_by('-id')
    setting = Setting.objects.first()
    context = {'category_list' : category_list, 'setting' : setting}
    return render(request, 'store/contact.html', context)

def products(request):
    category = request.GET.get('category')
    if category == None:
        product_list = Product.objects.all()
        category_list = Category.objects.all().order_by('-id')
        setting = Setting.objects.first()
        paginator = Paginator(product_list, 6)
        page_number = request.GET.get('page') #url ma dekni value get garni ani page_number ma rakhni
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

    else:
      product_list = Product.objects.filter(category__name = category) 
      category_list = Category.objects.all().order_by('-id')
      setting = Setting.objects.first()
      paginator = Paginator(product_list, 3)
      page_number = request.GET.get('page') #url ma dekni value get garni ani page_number ma rakhni
      page_obj = paginator.get_page(page_number) #tei page number lai garera pageobj ma halya
    context = {'product_list': product_list,'category_list' : category_list, 'setting': setting, 'page_obj':page_obj}
    return render(request, 'store/products.html', context)

def single(request, pk):
    single = Product.objects.get(pk=pk)
    category_list = Category.objects.all().order_by('-id')
    setting = Setting.objects.first()
    context = {'single' : single, 'category_list' : category_list, 'setting': setting}
    return render(request, 'store/single.html', context)

def brochure(request):
    pdf = Brochure.objects.first()
    context = {'pdf' : pdf}
    return render(request, 'store/pdf.html', context)

def searchbar(request):
    if 'query' in request.GET:
        query = request.GET['query']
        products = Product.objects.filter(Q(name__icontains=query) | Q(code__contains=query))
        return render(request, 'store/searchbar.html', {'products':products})

    else:
        print("No information to show")
        return render(request, 'store/searchbar.html', {})     


def checkout(request, pk):
    product = Product.objects.get(id=pk)    
    quantity = request.POST['quantity']         
    category_list = Category.objects.all().order_by('-id')
    setting = Setting.objects.first()
    
    print("request.method -------", request.method)
    # print('product!!!!!!!!!!!!!!!!!!', product_id)
    # print('product!!!!!!!!!!!!!!!!!!', request.method)
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST.get('email')
    #     phone = request.POST['phone']
    #     address = request.POST['address']
    #     quantity = request.POST['quantity']
    #     order = OrderItem(name=name,email=email,phone=phone,address=address,quantity=quantity)
    #     order.save()
    #     messages.success(request, 'Your message has been sent.')
    context = {'category_list':category_list, 'setting': setting, 'product':product, 'quantity': quantity}
    return render(request, 'store/checkout.html', context)

def completeCheckout(request):
    # print('product!!!!!!!!!!!!!!!!!!', product_id)
    # print('product!!!!!!!!!!!!!!!!!!', request.method)
    category_list = Category.objects.all().order_by('-id')[:4]
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        quantity = request.POST['quantity']
        id = request.POST['product_id']
        product = Product.objects.get(id=id)
        order = OrderItem(name=name,email=email,phone=phone,address=address,quantity=quantity,product=product)
        order.save()
        messages.success(request, 'Your message has been sent.')
    context = {'category_list':category_list}
    return render(request, 'store/checkout.html', context)
    # return redirect('/')