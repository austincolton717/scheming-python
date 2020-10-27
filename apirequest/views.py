from django.shortcuts import render, redirect


def apirequest(request):
    return render(request, 'requestfiles/apirequest.html', {})
