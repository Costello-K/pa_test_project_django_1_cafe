from django.contrib import admin
from .models import StartPage, About, WhyUsCard, DishCategory, Dish, Events, RestaurantPhoto, Chefs, Review

# Register your models here.
admin.site.register(StartPage)
admin.site.register(About)
admin.site.register(WhyUsCard)
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(RestaurantPhoto)
admin.site.register(Chefs)
admin.site.register(Review)
