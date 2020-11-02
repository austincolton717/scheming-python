from django import forms
from .models import clientData, clientNotes, clientProject, clientTasks, expenseInfo


class newClient(forms.ModelForm):

    class Meta:
        model = clientData
        fields = '__all__'


class newTask(forms.ModelForm):

    class Meta:
        model = clientTasks
        fields = '__all__'


class newProject(forms.ModelForm):

    class Meta:
        model = clientProject
        fields = '__all__'


class newNote(forms.ModelForm):

    class Meta:
        model = clientNotes
        fields = '__all__'


class newExpense(forms.ModelForm):

    class Meta:
        model = expenseInfo
        fields = '__all__'
