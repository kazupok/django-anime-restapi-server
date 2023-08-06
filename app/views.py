from rest_framework import viewsets, permissions
from .models import AnimeData, UserData, CustomerReview
from .serializers import AnimeDataSerializer, UserDataSerializer, CustomerReviewSerializer

class AnimeDataViewSet(viewsets.ModelViewSet):
    queryset = AnimeData.objects.all()
    serializer_class = AnimeDataSerializer


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.none()
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserData.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if not UserData.objects.filter(user=user).exists():
            serializer.save(user=user)


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer
