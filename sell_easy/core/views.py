# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def login(request):
#     return HttpResponse("User logged in")

# def signup(request):
#     return HttpResponse("User signed in")

# def dashboard(request):
#     return HttpResponse("Welcome to your dashboard ! ")


from django.shortcuts import render

from django.http import HttpResponse

from .models import Product, Store, Category, Rating

# Create your views here.

def index(request, id):
    print(request.method, id)
    return HttpResponse('Home Page')

"""def web_page(products):
        page = '<ul>'
        for product in products:
            page +=f"<li><h1>{product['name']}</h1><h2>{product['desc']}</h2><p>{product['price']}</p</li>"
            page +='<ul>'
        return page

def store_page(stores):
    page = '<ul>'
    for store in stores:
        page +=f"<li><h1>{store.name}</h1><h2>{store.tagline}</h2><p>{store.owner.username}, Welcome</p</li>"
        page +='<ul>'
    return page"""
def home(request):
    products = Product.objects.all()
    best_selling_products = products.filter('-price')[:4]
    products = products[:8]
    categories = Category.objects.all()[:4]
    stores = Store.objects.all()

    context={
        'products':products,
        'categories':categories,
        'stores':stores,
        'best_selling_products':best_selling_products,
        

    }
def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products, 'categories':categories}
    return render(request, 'core/products.html', context)

def product(request, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category)
    return render(request, 'core/detail.html', {'product':product, 'related_products':related_products})

def stores(request):
    pass

def store(request, id):
    pass

def stores_products(request, id):
    pass

def categories(request):
    pass

def category(request, id):
    pass