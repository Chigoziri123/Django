from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, NewsletterSubscriber
# Create your views here.

def signup (request):
    return render(request, 'blogapp/signup.html')

def login (request):
    return render(request, 'blogapp/login.html')

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blogapp/dashboard.html', {'articles': articles})

@login_required
def create_article(request):
    if request.method == "POST":
        # process form data and save the article
        return redirect('dashboard')
    return render(request, 'create_article.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles':articles})

@login_required
def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        #process form data and update the article
        return redirect('dashboard')
    return render(request, 'update_article.html', {'article': article})

def archive_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        # archive the article
        return redirect('dashboard')
    return render(request, 'blogapp/archive_article.html', {'article': article})


def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('dashboard')
    return render(request, 'blogapp/delete_article.html', {'article':article})


def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscriber = NewsletterSubscriber(email=email)
        subscriber.save()
        messages.success(request, 'Subscribed successfully to the newsletter')
        return redirect('article_list')
    return render(request, 'blogapp/subscribe_newsletter.html')


