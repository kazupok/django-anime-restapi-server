from django.contrib import admin
from .models import AnimeData, UserData, CustomerReview

admin.site.register(UserData)
admin.site.register(AnimeData)
admin.site.register(CustomerReview)
