from itertools import product
from django import forms
from django.shortcuts import render
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'equipment_type', 'power', 'region', 'image', 'phone_number', 'telegram_username', 'instagram_username']
        widgets = {
            'equipment_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'power': forms.NumberInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (XXX) XXX-XX-XX'}),
            'telegram_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@username'}),
            'instagram_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@username'}),
        }
class ProductFilterForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)

def filter_products(request):
    if request.method == 'GET':
        form = ProductFilterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = product.objects.filter(name__icontains=query)
            return render(request, 'products.html', {'products': products})
    else:
        form = ProductFilterForm()
    return render(request, 'filter.html', {'form': form})