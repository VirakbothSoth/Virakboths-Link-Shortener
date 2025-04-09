from django.urls import path
from . import views

urlpatterns = [
    path("", views.shorten_url, name="shorten_url"),
    path('signup/', views.signup_view, name='signup'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("user_links/", views.user_links, name="user_links"),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
    path('delete/<str:short_code>/', views.delete_link, name='delete_link'),
]