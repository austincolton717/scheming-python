from django.shortcuts import render, redirect


def pbnlist(request):
    return render(request, 'pbnfiles/pbnlist.html', {})
