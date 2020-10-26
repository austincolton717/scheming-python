from django.shortcuts import render, redirect


def indexautomation(request):
    return render(request, 'automationfiles/indexautomation.html', {})
