from django.shortcuts import render


# Create your views here.
def news_page(request):
    return render(request, 'news/index.html')


# just for testing
def news_detail(request):
    return render(request, 'news/single.html')


# just for testing
def news_category(request):
    return render(request, 'news/category.html')


# just for testing
def contact(request):
    return render(request, 'news/contact.html')
