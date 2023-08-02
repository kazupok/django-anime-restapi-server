from rest_framework import viewsets
from .models import AnimeData, UserData, CustomerReview
from .serializers import AnimeDataSerializer, UserDataSerializer, CustomerReviewSerializer

class AnimeDataViewSet(viewsets.ModelViewSet):
    queryset = AnimeData.objects.all()
    serializer_class = AnimeDataSerializer


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer
