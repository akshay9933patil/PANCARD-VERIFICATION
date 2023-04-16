from django.urls import path
from .views import verification_view


urlpatterns = [
    path('form/', verification_view)
]