from django.shortcuts import render, redirect


def archive(request):
    return render(request, 'archivefiles/archive.html', {})
