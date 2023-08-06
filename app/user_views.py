from rest_framework import viewsets, permissions, response
from django.contrib.auth.models import User
from .user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # ユーザー登録は誰でも可能に設定

    def list(self, request):
        if request.user.is_authenticated:
            queryset = User.objects.filter(id=request.user.id)
            serializer = UserSerializer(queryset, many=True)
            return response.Response(serializer.data)
        else:
            return response.Response(status=401)  # Unauthorized