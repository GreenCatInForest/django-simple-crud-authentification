from django.urls import path
from .views import register_user, user_login, user_logout, home_page_url_name, special_page_url_name

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home_page_url_name/', home_page_url_name, name='home_page_url_name'),
    path('special_page_url_name', special_page_url_name, name='special_page_url_name')
]