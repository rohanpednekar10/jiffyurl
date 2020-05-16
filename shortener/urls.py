from django.urls import path
from .views import HomeView, ShortenerView, AnalyticsView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shortener/', ShortenerView.as_view(), name='shortener'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]