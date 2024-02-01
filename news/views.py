from django.shortcuts import render

from news.models import News, Comment, NewsCategory


# Create your views here.
def news_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all().order_by('-id')
    sport_news = News.objects.filter(category_id__name='SPORT').order_by('-id')
    uzb_news = News.objects.filter(category_id__name='O‘ZBEKISTON').order_by('-id')
    world_news = News.objects.filter(category_id__name='JAHON').order_by('-id')[:4]  # 4 ta bo'lishi kerak shuning uchun [:4]
    trending_news = News.objects.all().order_by('-views')[:3]  # 3 ta bo'lishi kerak shuning uchun [:3]
    context = {
        'news': news,
        'sport_news': sport_news,
        'uzb_news': uzb_news,
        'categories': categories,
        'world_news': world_news,
        'trending_news': trending_news
    }
    return render(request, 'news/index.html', context=context)


def news_detail(request, pk):
    categories = NewsCategory.objects.all()  # barcha kategoriyalarni olish
    single_news = News.objects.get(id=pk)  # qaysi yangilikni ichiga kirgan bo'lsa shu yangilikni olish
    breaking_uzb_news = News.objects.filter(category_id__name='O‘ZBEKISTON').order_by('-id')  # yurtimizga doir degan joyga yangiliklarni filtrlab olish
    news_comments = Comment.objects.filter(news_id=single_news)  # shu yangilikga tegishli commentlarni olish
    trending_news = News.objects.all().order_by('-views')[:3]  # 3 ta bo'lishi kerak shuning uchun [:3]
    context = {
        'single_news': single_news,
        'breaking_uzb_news': breaking_uzb_news,
        'news_comments': news_comments,
        'categories': categories,
        'trending_news': trending_news
    }
    return render(request, 'news/single.html', context=context)


def news_category(request, slug):
    categories = NewsCategory.objects.all()
    category = NewsCategory.objects.get(slug=slug)
    news = News.objects.filter(category_id=category)
    trending_news = News.objects.all().order_by('-views')[:3]  # 3 ta bo'lishi kerak shuning uchun [:3]
    context = {
        'category': category,
        'news': news,
        'categories': categories,
        'trending_news': trending_news
    }
    return render(request, 'news/category.html', context=context)


# just for testing
def contact(request):
    categories = NewsCategory.objects.all()
    trending_news = News.objects.all().order_by('-views')[:3]  # 3 ta bo'lishi kerak shuning uchun [:3]
    context = {
        'categories': categories,
        'trending_news': trending_news
    }
    return render(request, 'news/contact.html', context=context)
