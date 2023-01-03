from datetime import datetime
from django.shortcuts import render, redirect
from .models import StartPage, About, WhyUsCard, DishCategory, Dish, Events, RestaurantPhoto, Chefs, Review
    # , Maps
from .forms import FormUserReservation, FormUserMessage

MAX_QUANTITY_START_PAGES_SLIDES = 5
MAX_QUANTITY_OF_PHOTOS_IN_GALLERY_DISPLAYED = 8
MAX_QUANTITY_REVIEWS_DISPLAYED = 10


# Create your views here.
def main_page(request):
    popup_reservation, popup_message, not_valid_form = False, False, False

    if request.method == 'POST':
        form_user_reservation = FormUserReservation(request.POST)
        form_user_messages = FormUserMessage(request.POST)
        if form_user_reservation.is_valid():
            form_user_reservation.save()
            popup_reservation = True
            # return redirect('/')
        elif form_user_messages.is_valid():
            form_user_messages.save()
            popup_message = True
            # return redirect('/')
        else:
            not_valid_form = True

    start_page = StartPage.objects.filter(is_visible=True)[:MAX_QUANTITY_START_PAGES_SLIDES]
    about = About.objects.first()
    cards = WhyUsCard.objects.filter(is_visible=True)[:3]
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True, date_stop_event__gt=datetime.now())
    gallery = RestaurantPhoto.objects.filter(is_visible=True)[:MAX_QUANTITY_OF_PHOTOS_IN_GALLERY_DISPLAYED]
    chefs = Chefs.objects.filter(is_visible=True)
    reviews = Review.objects.filter(is_visible=True)[:MAX_QUANTITY_REVIEWS_DISPLAYED]
    form_user_reservation = FormUserReservation()
    form_user_message = FormUserMessage()
    # maps = Maps()

    return render(request, 'main_page.html', context={
        'start_page': start_page,
        'about': about,
        'cards': cards,
        'categories': categories,
        'dishes': dishes,
        'specials': specials_dishes,
        'events': events,
        'gallery': gallery,
        'chefs': chefs,
        'reviews': reviews,
        'form_user_reservation': form_user_reservation,
        'form_user_message': form_user_message,
        'popup_reservation': popup_reservation,
        'popup_message': popup_message,
        'not_valid_form': not_valid_form,
        # 'maps': maps,
    })
