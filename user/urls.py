from django.urls import path

from .views import login , Register

urlpatterns = [
    path('login/', login),
    path('sign_up/', Register)

]
