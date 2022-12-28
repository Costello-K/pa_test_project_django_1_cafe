from django.urls import path
from .views import reservations, messages, update_reservations, update_messages

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservations, name='reservations'),
    path('reservations/update/<int:pk>/', update_reservations, name='update_reservations'),
    path('messages/', messages, name='messages'),
    path('messages/update/<int:pk>/', update_messages, name='update_messages'),
]
