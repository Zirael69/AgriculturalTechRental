from django.urls import path
from .views import HomePageview, AboutPageView

urlpatterns = [
    path('', HomePageview.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
