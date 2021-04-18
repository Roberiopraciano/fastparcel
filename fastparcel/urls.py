from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('',views.home),

    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/',views.sign_up),

    path('customer/',views.customer_page),
    path('courier/',views.courier_page),
    path(r'^error_page/$', views.ErrorPage.as_view(), name="error-page"),
    
]
