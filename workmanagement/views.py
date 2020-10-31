from django.shortcuts import render, redirect
from .models import seoProject
from .forms import newProject
from django.http import HttpResponse


def workManagement(request):
    return render(request, 'workfiles/workmanagement.html', {})


def projects(request):
    projectshelf = seoProject.objects.all()
    return render(request, 'workfiles/projects.html', {'projectshelf': projectshelf})


def upload_project(request):
    upload = newProject()
    if request.method == 'POST':
        upload = newProject(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('projects')
        else:
            return HttpResponse("""your form has errors, reload on <a href = "{{ url : 'projects'}}">reload</a>""")
    else:
        return render(request, 'workfiles/addproject.html', {'addproject': upload})


def update_project(request, project_id):
    project_id = int(project_id)
    try:
        project_sel = seoProject.objects.get(id=project_id)
    except seoProject.DoesNotExist:
        return redirect('projects')
    project_form = newProject(request.POST or None, instance=project_sel)
    if project_form.is_valid():
        project_form.save()
        return redirect('projects')
    return render(request, 'workfiles/addproject.html', {'addproject': project_form})


def delete_project(request, project_id):
    project_id = int(project_id)
    try:
        project_sel = seoProject.objects.get(id=project_id)
    except seoProject.DoesNotExist:
        return redirect('projects')
    project_sel.delete()
    return redirect('projects')


def project_info(request, project_id):
    project_id = int(project_id)
    return redirect('projects')
