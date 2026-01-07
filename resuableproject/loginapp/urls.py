from django.urls import path
from loginapp import views

urlpatterns = [
    path('login/', views.register_view),
    path('result/', views.login_view),
    path('leave/', views.logout_view),
]