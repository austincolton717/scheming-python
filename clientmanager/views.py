from django.shortcuts import render, redirect


def clientManager(request):
    return render(request, 'clientfiles/clientmanager.html', {})
