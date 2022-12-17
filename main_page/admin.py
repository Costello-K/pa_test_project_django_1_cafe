from django.contrib import admin
from .models import About, WhyUsCard, DishCategory, Dish, Events

# Register your models here.
admin.site.register(About)
admin.site.register(WhyUsCard)
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Events)
