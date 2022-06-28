from django.urls import include, path
from .views import ticketView,HomeView

urlpatterns = [
    path('create', ticketView, name="ticket"),
        path('',HomeView,name='home')

]