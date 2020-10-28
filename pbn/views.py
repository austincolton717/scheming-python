from django.shortcuts import render, redirect
from .forms import ListForm
from .models import List


def pbnlist(request):
    return render(request, 'pbnfiles/pbnlist.html', {})
