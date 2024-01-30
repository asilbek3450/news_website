from django.urls import path
from .views import news_page, news_detail, news_category, contact

urlpatterns = [
    path('', news_page, name='news_page'),
    path('single/', news_detail, name='news_detail'),
    path('category/', news_category, name='news_category'),
    path('contact/', contact, name='contact'),

]
