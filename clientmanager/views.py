from django.shortcuts import render, redirect
from .models import clientTasks, clientProject, clientNotes, clientData, expenseInfo
from .forms import newProject, newNote, newTask, newExpense, newClient
from django.http import HttpResponse


def clientManager(request):
    clientshelf = clientData.objects.all()
    return render(request, 'clientfiles/clientmanager.html', {'clientshelf': clientshelf})


def upload_client(request):
    upload = newClient()
    if request.method == 'POST':
        upload = newClient(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('clientmanager')
        else:
            return HttpResponse("""your form has errors, reload on <a href = "{{ url : 'clientmanager'}}">reload</a>""")
    else:
        return render(request, 'clientfiles/addclient.html', {'addclient': upload})


def update_client(request, client_id):
    client_id = int(client_id)
    try:
        client_sel = clientData.objects.get(id=client_id)
    except clientData.DoesNotExist:
        return redirect('clientmanager')
    client_form = newClient(request.POST or None, instance=client_sel)
    if client_form.is_valid():
        client_form.save()
        return redirect('clientmanager')
    return render(request, 'clientfiles/addclient.html', {'addclient': client_form})


def delete_client(request, client_id):
    client_id = int(client_id)
    try:
        client_sel = clientData.objects.get(id=client_id)
    except clientData.DoesNotExist:
        return redirect('clientmanager')
    client_sel.delete()
    return redirect('clientmanager')
