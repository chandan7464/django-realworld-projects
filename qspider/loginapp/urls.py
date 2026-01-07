from django.urls import path
from loginapp import views

urlpatterns = [
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path("base/",views.base_view),
]