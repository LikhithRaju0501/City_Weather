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
        if api['data']['iaqi']['pm25']['v'] > 50 and api['data']['iaqi']['pm25']['v'] <= 100:
            color = "moderate"
            content_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
        elif api['data']['iaqi']['pm25']['v'] > 100 and api['data']['iaqi']['pm25']['v'] <= 150:
            color = "usg"
            content_description = "(101-151) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        elif api['data']['iaqi']['pm25']['v'] > 150 and api['data']['iaqi']['pm25']['v'] <= 200:
            color = "unhealthy"
            content_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif api['data']['iaqi']['pm25']['v'] > 200 and api['data']['iaqi']['pm25']['v'] <= 250:
            color = "veryunhealthy"
            content_description = "(201-250) Health alert: everyone may experience more serious health effects."
        elif api['data']['iaqi']['pm25']['v'] > 250 and api['data']['iaqi']['pm25']['v'] <= 300:
            color = "hazardous"
            content_description = "(251-300) Health warnings of emergency conditions. The entire population is more likely to be affected"
        else:
            color = "good"
            content_description = "(0 - 50)Air quality is considered satisfactory, and air pollution poses little or no risk."
        return render(request , 'home.html' , {'api':api , 'color':color , 'content_description':content_description})
    else :
        api_request = requests.get("https://api.waqi.info/feed/london/?token=9cb752c294cf777f37b2ad164a6096d71e885f3a")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request , 'home.html' , {'api':api})


def about(request):
    return render(request , 'about.html' , {})
