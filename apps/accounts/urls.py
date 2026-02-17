from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_login,profile
urlpatterns = [
    path('login/',user_login),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('profile/', profile, name='profile'),
    # path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

]