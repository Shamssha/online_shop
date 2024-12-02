
import itertools
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from shop_order.forms import UserNewOrder
from .forms import LoginForm, RegisterForm
from .models import Catagory, Product, Brand, ProductGalary
from django.db.models import Q

# Create your views here.
# --------------------product list ------------------------------
def product_list(request):
    pr_list = Product.objects.all()
    paginator = Paginator(pr_list, 4)
    page_namber = request.GET.get('page')
    page_obj = paginator.get_page(page_namber)
    brand = Brand.objects.all()
    brand_grouper = list(list_grouper(4,brand))
    context = {
        "list": pr_list,
        "brands": brand_grouper,
        'page_obj': page_obj,
    }
    return render(request, 'shop.html', context)
# -------------------products details -----------------------
def list_grouper(n,iterable):
    args = [iter(iterable)]*n
    return([e for e in t if e is not None] for t in itertools.zip_longest(*args))

@login_required(login_url=product_list)
def product(request, slug, *args, **kwargs):
    # get_product_id = kwargs['_id']
    product_page = Product.objects.get(id=slug)
    product_galary = ProductGalary.objects.filter(product_id=product_page)
    group_galary = list(list_grouper(3, product_galary))
    related_product = Product.objects.get_queryset().filter(pr_catagory__product=product_page)
    group_related = list(list_grouper(2, related_product))
    # order form
    new_order_form = UserNewOrder(request.POST or None, initial=({'product_id':product_page}))
    # print(id)
    context = {
        'product': product_page,
        'product_galary': product_galary,
        'group_galary':group_galary,
        'related':related_product,
        'group_related':group_related,
        # order form
        'order_form':new_order_form,
    }
    return render(request, 'product.html', context)
# ---------------------login page -------------------
def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        userName = login_form.cleaned_data.get('userName')
        print(userName)
        password = login_form.cleaned_data.get('password')
        print(password)
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("شما موفقانه وارد شدید"))
            return redirect(product_list)

        else:
            messages.success(request, ("مشکلی پیش آمد"))

    context = {
        'message': 'موفقانه وارد شدید.',
        'login_form': login_form
    }

    return render(request, 'auth/login.html', context)
# ---------------logout page----------------------------


def logout_page(request):
    logout(request)
    messages.success(request, ('باموفقیت خارج شدید'))
    return redirect("list")
# ----------------Register Views ---------------------------


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        userName = register_form.cleaned_data.get('userName')
        print(userName)
        email = register_form.cleaned_data.get('email')
        print(email)
        password = register_form.cleaned_data.get('password')
        print(password)
        new_user = User.objects.create_user(
            username=userName, email=email, password=password)
    context = {
        'title': 'register page',
        'register_form': register_form
    }
    return render(request, 'auth/register.html', context)

# ------------Search views-----------------------


def search(request):
    if 'q' in request.GET and request.GET['q']:
        sher = request.GET.get('q')
        lockup = Q(pr_name__icontains=sher) | Q(pr_discription__icontains=sher)
        pr_search = Product.objects.filter(lockup)
        # paginator = Paginator(pr_search,4)
        # page_namber = request.GET.get('page')
        # page_obj = paginator.get_page(page_namber)
        paginator = Paginator(pr_search, 2)
        page_namber = request.GET.get('page')
        page_obj = paginator.get_page(page_namber)

        return render(request, 'shop.html', {'page_obj': page_obj, 'search': pr_search})
    else:
        return render(request, 'shop.html')

# -----------------------Catagory----------------------------------


def catagoryView(request, cat):
    cat = cat.replace("-", " ")
    # try:
    catagory_list = Catagory.objects.get(name=cat)
    catagory_objects = Catagory.objects.all()
    products = Product.objects.filter(pr_catagory=catagory_list)

    paginator = Paginator(products, 4)
    page_namber = request.GET.get('page')
    page_obj = paginator.get_page(page_namber)

    context = {
        'catagory_objects': catagory_objects,
        'products': products,
        'page_obj': page_obj,
        'catagory_list': catagory_list
    }
    return render(request, 'catagory.html', context)


def catagory_partcial(request):
    catagory_objects = Catagory.objects.all()
    context = {
        'catagory_objects': catagory_objects
    }
    return render(request, 'catagory_partial.html',context)

    # except:
    # messages.success(request,('دسته بندی وجود ندارد'))
    # return redirect(product_list)
# ====================Brand==================
def brand(request):
    brand_img = Brand.objects.filter(brand_img)