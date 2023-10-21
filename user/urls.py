from django.urls import path

from .views import login , Register , logout

urlpatterns = [
    path('login/', login),
    path('sign_up/', Register),
    path('logout/', logout),

]
