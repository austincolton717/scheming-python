from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.http import *
from googlesearch import search
import os


def indexautomation(request):
    return render(request, 'automationfiles/indexautomation.html', {})


def indexChecker(request):
    if request.method == 'POST' and request.POST['input_list']:
        text_object = request.POST['input_list']
        query = text_object.splitlines()

        def indexBoolean(s):
            for i in search(s,
                            lang='en',
                            stop=50,
                            pause=2.0,
                            ):
                return True
            return False

        results = []
        for website in query:
            result = [website, str(indexBoolean("site:" + website))]
            print(result)
            results.append(result)

        resp = HttpResponse(results, content_type='application/x-download')
        return resp
    return render(request, 'automationfiles/indexchecker.html', {})
