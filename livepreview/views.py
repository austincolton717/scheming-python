from django.shortcuts import render, redirect


def preview(request):
    return render(request, 'previewfiles/preview.html', {})
