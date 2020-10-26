from django.shortcuts import render, redirect


def workManagement(request):
    return render(request, 'workfiles/workmanagement.html', {})
