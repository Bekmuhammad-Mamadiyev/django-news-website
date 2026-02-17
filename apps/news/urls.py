from django.urls import path
from .views import (new_detail, home_views, ContactPageview, WorldNewsView, NewsDeleteView,
                    NewsUpdateView, NewsCreateView)

urlpatterns = [
    path('', home_views, name='home_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('contact/', ContactPageview.as_view(), name='contact_page'),
    path('world/',WorldNewsView.as_view() , name='world_news'),
    path('<slug:news>/', new_detail, name='news_detail'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('<slug>/update/', NewsUpdateView.as_view(), name='news_update'),

]