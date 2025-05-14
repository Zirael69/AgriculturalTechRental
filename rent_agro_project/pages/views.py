from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomePageview(ListView):
    model = Post
    template_name ='home.html'

class AboutPageView(ListView):
    model = Post
    template_name ='about.html'

class HomePageview(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = '/accounts/login/' 
