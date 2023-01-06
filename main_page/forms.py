import json
from django import forms
from django.contrib import admin
from .models import UserReservation, UserMessage
    # , Rental
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


# class RentalAdmin(admin.ModelAdmin):
#
#     class Meta:
#         model = Rental
#         fields = ('formfield_overrides', )
#
#     formfield_overrides = map_fields.AddressField(widget=map_widgets.GoogleMapsAddressWidget(attrs={
#                 'data-autocomplete-options': json.dumps({'types': ['geocode', 'establishment'], 'componentRestrictions': {'country': 'uk'}})
#                                                   }))


class FormUserReservation(forms.ModelForm):

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'persons', 'message', 'future_date_reserve', 'future_time_reserve')

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "name",
                                'class': "form-control",
                                'id': "name",
                                'placeholder': "Ваше ім'я",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"})
                           )
    email = forms.EmailField(max_length=70, widget=forms.TextInput(attrs={
                                'type': "email",
                                'name': "email",
                                'class': "form-control",
                                'id': "email",
                                'placeholder': "Ваш e-mail",
                                'data-rule': "email",
                                'data-msg': "Please enter a valid email"})
                             )
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "phone",
                                'class': "form-control",
                                'id': "phone",
                                'placeholder': "Ваш телефон",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"})
                            )
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                                'type': "number",
                                'min': '1',
                                'name': "people",
                                'class': "form-control",
                                'id': "people",
                                'rows': "5",
                                'placeholder': "Кількість людей",
                                'data-rule': "minlen:1",
                                'data-msg': "Please enter at least 1 chars"})
                                )
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                'name': "message",
                                'class': "form-control",
                                'rows': "5",
                                'placeholder': "Повідомлення"})
                              )
    future_date_reserve = forms.DateField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "date",
                                'class': "form-control",
                                'id': "date",
                                'placeholder': "Дата",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"})
                                          )
    future_time_reserve = forms.TimeField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'name': "time",
                                'id': "time",
                                'placeholder': "Час",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"})
                                          )


class FormUserMessage(forms.ModelForm):

    class Meta:
        model = UserMessage
        fields = ('name', 'email', 'subject_message', 'message')

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "name",
                                'class': "form-control",
                                'id': "name",
                                'placeholder': "Ваше ім'я"})
                           )
    email = forms.EmailField(max_length=70, widget=forms.TextInput(attrs={
                                'type': "email",
                                'name': "email",
                                'class': "form-control",
                                'id': "email",
                                'placeholder': "Ваш e-mail"})
                             )
    subject_message = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "subject",
                                'class': "form-control",
                                'id': "subject",
                                'placeholder': "Тема повідомлення"})
                                      )
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                'name': "message",
                                'class': "form-control",
                                'rows': "5",
                                'placeholder': "Повідомлення"})
                              )
