from django.shortcuts import render, redirect
from main_page.models import UserReservation, UserMessage
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations(request):
    user_reservations = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={'reservations': user_reservations})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def messages(request):
    user_messages = UserMessage.objects.filter(is_processed=False)
    return render(request, 'messages.html', context={'messages': user_messages})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservations(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_messages(request, pk):
    UserMessage.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:messages')
