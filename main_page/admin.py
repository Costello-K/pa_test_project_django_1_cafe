from django.contrib import admin
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import StartPage, About, WhyUsCard, DishCategory, Dish, Events, RestaurantPhoto, Chefs, Review, \
    UserReservation, UserMessage\
    # , Maps

# Register your models here.
# admin.site.register(Maps)
admin.site.register(StartPage)
admin.site.register(About)
admin.site.register(WhyUsCard)
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(RestaurantPhoto)
admin.site.register(Chefs)
admin.site.register(Review)
admin.site.register(UserReservation)
admin.site.register(UserMessage)


# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#             'widget': map_widgets.GoogleMapsAddressWidget(attrs={
#                 'data-autocomplete-options': json.dumps({'types': ['geocode', 'establishment'],
#                                                          'componentRestrictions': {'country': 'us'}
#                                                          })})}}
