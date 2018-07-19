from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour

def main_grid(request):
    tour_list = Tour.objects.all()
    return render(request, 'tour/tour_list.html', {'tour_list': tour_list})

