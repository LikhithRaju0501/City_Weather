from django.shortcuts import render

def home(request):
    import json
    import requests
    if request.method == "POST" :
        place = request.POST['place']
        api_request = requests.get("https://api.waqi.info/feed/"+ place + "/?token=9cb752c294cf777f37b2ad164a6096d71e885f3a")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request , 'home.html' , {'api':api})
    else :
        api_request = requests.get("https://api.waqi.info/feed/london/?token=9cb752c294cf777f37b2ad164a6096d71e885f3a")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request , 'home.html' , {'api':api})


def about(request):
    return render(request , 'about.html' , {})
