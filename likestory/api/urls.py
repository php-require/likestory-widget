from django.urls import path

from .views import likeAPIView

urlpatterns = [
    path('test-api/', likeAPIView.as_view(), name='test')
]