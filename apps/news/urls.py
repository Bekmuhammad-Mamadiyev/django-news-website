from django.urls import path
from .views import news_list, new_detail, home_views, contact_views

urlpatterns = [
    path('home/', home_views),
    path('contact/', contact_views),
    path('all/', news_list, name='news_list'),
    path('all/<slug:slug>/', new_detail, name='birnima'),
]