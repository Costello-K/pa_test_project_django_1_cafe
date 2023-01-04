from django.contrib import admin
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import StartPage, About, WhyUsCard, DishCategory, Dish, Events, RestaurantPhoto, Chefs, Review, \
    UserReservation, UserMessage
    # , Maps

# Register your models here.
# admin.site.register(Maps)
admin.site.register(About)


@admin.register(StartPage)
class StartPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'is_visible']
    list_display_links = ['title']
    list_filter = ['is_visible']
    list_editable = ['is_visible', 'photo']


@admin.register(WhyUsCard)
class WhyUsCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_visible']
    list_display_links = ['title']
    list_filter = ['is_visible']
    list_editable = ['is_visible']


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible']
    list_display_links = ['name']
    list_filter = ['is_visible']
    list_editable = ['is_visible']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'category', 'price', 'ingredients', 'photo', 'description', 'is_special']
    list_display_links = ['name']
    list_filter = ['is_visible', 'category', 'is_special', 'price']
    list_editable = ['is_visible', 'is_special', 'price', 'photo']
    search_fields = ('name', 'category')
    list_max_show_all = 100


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_stop_event', 'price', 'photo', 'description', 'is_visible']
    list_display_links = ['title']
    list_filter = ['is_visible', 'date_stop_event', 'price']
    list_editable = ['is_visible', 'date_stop_event', 'price', 'photo']


@admin.register(RestaurantPhoto)
class RestaurantPhotoAdmin(admin.ModelAdmin):
    list_display = ['position', 'photo', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['is_visible', 'photo']


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'profession', 'photo', 'is_visible']
    list_display_links = ['name']
    list_filter = ['name', 'surname', 'is_visible']
    list_editable = ['is_visible', 'photo']


@admin.register(UserReservation)
class UserReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'is_processed', 'phone', 'persons', 'future_date_reserve', 'future_time_reserve']
    list_display_links = ['name']
    list_filter = ['is_processed', 'date', 'persons', 'future_date_reserve', 'future_time_reserve']
    list_editable = ['is_processed', 'persons', 'future_date_reserve', 'future_time_reserve']
    search_fields = ('name', )
    list_max_show_all = 50


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'is_processed', 'subject_message', 'email']
    list_display_links = ['subject_message']
    list_filter = ['is_processed', 'date', 'name']
    list_editable = ['is_processed']
    search_fields = ('name', )
    list_max_show_all = 50


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'profession', 'rating', 'is_visible']
    list_display_links = ['name']
    list_filter = ['name', 'surname', 'rating']
    list_editable = ['is_visible']
    search_fields = ('rating', )
    list_max_show_all = 50


# @admin.register(RentalAdmin)
# class RentalAdminAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#             'widget': map_widgets.GoogleMapsAddressWidget(attrs={
#                 'data-autocomplete-options': json.dumps({'types': ['geocode', 'establishment'],
#                                                          'componentRestrictions': {'country': 'us'}
#                                                          })})}}
