from datetime import datetime
from django.shortcuts import render
from .models import About, WhyUsCard, DishCategory, Dish, Events, RestaurantPhoto, Chefs, Review


# Create your views here.
def main_page(request):
    about = About.objects.first()
    cards = WhyUsCard.objects.filter()
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True, date_stop_event__gt=datetime.now())
    gallery = RestaurantPhoto.objects.filter(is_visible=True)
    chefs = Chefs.objects.filter(is_visible=True)
    reviews = Review.objects.filter(is_visible=True)
    return render(request, 'main_page.html', context={
        'about': about,
        'cards': cards,
        'categories': categories,
        'dishes': dishes,
        'specials': specials_dishes,
        'events': events,
        'gallery': gallery,
        'chefs': chefs,
        'reviews': reviews,
    })
