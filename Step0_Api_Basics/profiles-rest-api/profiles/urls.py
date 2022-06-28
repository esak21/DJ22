from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register('hvs', views.HelloViewSets, basename='hvs')

# basename is needed if ur serializer doesnt have any queryset or we need to override the name of the qoery set 
router.register('profile', views.UserProfileViewSets)
router.register('feeds', views.UserProfileFeedViewSet)

urlpatterns = [
    path("", views.HelloApiView.as_view()),
    path('v1/', include(router.urls)),
    path("login/", views.UserLoginApiView.as_view())

]