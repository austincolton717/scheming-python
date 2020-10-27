from django.shortcuts import render, redirect
from .forms import ListForm
from .models import List


def pbnlist(request):

    # if request.method == 'POST':
    #     form = ListForm(request.POST or None)

    #     if form.is_valid():
    #         form.save()
    #         all_items = List.objects.all
    #         return render(request, 'pbnfiles/pbnlist.html', {'all_itms': all_items})

    #     else:
    #         all_items = List.objects.all
    #         return render(request, 'pbnfiles/pbnlist.html', {'all_items': all_items})
    return render(request, 'pbnfiles/pbnlist.html', {})
