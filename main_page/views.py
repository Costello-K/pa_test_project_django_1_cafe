from django.shortcuts import render
from .models import About, WhyUsCard, DishCategory, Dish, Events


# Create your views here.
def main_page(request):
    about = About.objects.first()
    cards = WhyUsCard.objects.filter()
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    return render(request, 'main_page.html', context={
        'about': about,
        'cards': cards,
        'categories': categories,
        'dishes': dishes,
        'specials': specials_dishes,
        'events': events
    })
