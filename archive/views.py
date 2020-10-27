from django.shortcuts import render


def archive(request):
    import requests
    import json

    api_request = requests.get(
        "https://apiv2.ahrefs.com?token=b980fbffd773d102a44a203a21c1aeaa2cb34604&target=ahrefs.com&limit=10&output=json&from=ahrefs_rank&mode=domain")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'archivefiles/archive.html', {'api': api})
