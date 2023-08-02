from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimeDataViewSet, UserDataViewSet, CustomerReviewViewSet

router = DefaultRouter()
router.register(r'anime', AnimeDataViewSet)
router.register(r'user', UserDataViewSet)
router.register(r'review', CustomerReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
