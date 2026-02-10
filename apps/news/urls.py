from django.urls import path
from .views import new_detail, home_views, ContactPageview, WorldNewsView

urlpatterns = [
    path('home/', home_views, name='home_page'),
    path('contact/', ContactPageview.as_view(), name='contact_page'),
    path('world/',WorldNewsView.as_view() , name='world_news'),
    path('<slug:news>/', new_detail, name='news_detail'),

]