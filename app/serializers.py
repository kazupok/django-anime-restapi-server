from rest_framework import serializers
from .models import AnimeData, UserData, CustomerReview

class AnimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeData
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = '__all__'
