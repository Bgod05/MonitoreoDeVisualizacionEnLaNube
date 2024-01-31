from django.urls import path

from .views import show_user_data

urlpatterns = [
    path('', show_user_data)
]
