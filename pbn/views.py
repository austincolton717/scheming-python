from django.shortcuts import render, redirect
from .models import PBNsite
from .forms import NewPbn
from django.http import HttpResponse


def pbnlist(request):
    shelf = PBNsite.objects.all()
    return render(request, 'pbnfiles/pbnlist.html', {'shelf': shelf})


def upload_pbn(request):
    upload = NewPbn()
    if request.method == 'POST':
        upload = NewPbn(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('pbnlist')
        else:
            return HttpResponse("""your form has errors, reload on <a href = "{{ url : 'pbn'}}">reload</a>""")
    else:
        return render(request, 'pbnfiles/addpbn.html', {'addpbn': upload})


def update_pbn(request, pbn_id):
    pbn_id = int(pbn_id)
    try:
        pbn_sel = PBNsite.objects.get(id=pbn_id)
    except PBNsite.DoesNotExist:
        return redirect('pbnlist')
    pbn_form = NewPbn(request.POST or None, instance=pbn_sel)
    if pbn_form.is_valid():
        pbn_form.save()
        return redirect('pbnlist')
    return render(request, 'pbnfiles/addpbn.html', {'addpbn': pbn_form})


def delete_pbn(request, pbn_id):
    pbn_id = int(pbn_id)
    try:
        pbn_sel = PBNsite.objects.get(id=pbn_id)
    except PBNsite.DoesNotExist:
        return redirect('pbnlist')
    pbn_sel.delete()
    return redirect('pbnlist')
