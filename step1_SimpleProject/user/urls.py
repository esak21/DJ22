from django.urls import include, path
from .views import indexView, HomeView

urlpatterns = [
    path('createuser', indexView, name="index"),
    path('',HomeView,name='home')
]