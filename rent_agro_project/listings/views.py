from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ListingForm
from .models import Listing


def is_owner(user):
    return user.is_authenticated and getattr(user, 'role', '') == 'owner'


@login_required
@user_passes_test(is_owner, login_url='post_list')
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            print(f"Сохранено объявление: {listing.title}")  # Отладка
            print(f"Контакты: phone={listing.phone_number}, telegram={listing.telegram_username}, instagram={listing.instagram_username}")  # Отладка
            return redirect('post_list')
    else:
        form = ListingForm()
    return render(request, 'posts/create_post.html', {'form': form})


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'posts/detail.html', {'listing': listing})


def post_list(request):
    listings = Listing.objects.all()

    type_filter = request.GET.get('type')
    brand_filter = request.GET.get('brand')
    max_price = request.GET.get('max_price')
    min_power = request.GET.get('min_power')

    if type_filter:
        listings = listings.filter(equipment_type__iexact=type_filter)

    if brand_filter:
        brand_filter = brand_filter.strip()
        if brand_filter:
            listings = listings.filter(brand__icontains=brand_filter)

    if max_price:
        try:
            listings = listings.filter(price__lte=int(max_price))
        except ValueError:
            pass

    if min_power:
        try:
            listings = listings.filter(power__gte=int(min_power))
        except ValueError:
            pass

    context = {
        'listings': listings,
    }

    return render(request, 'posts/post_list.html', context)
