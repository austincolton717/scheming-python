from django.shortcuts import render, redirect


def seoDataTools(request):
    return render(request, 'seofiles/seodatatools.html', {})
