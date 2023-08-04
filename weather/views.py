from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
  json_dic = {}
  if request.method == 'POST':
    city = request.POST['city']
    my_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=9cda8a49405d88e9e5794a5ce30769ff').read()
    json_data = json.loads(my_url)
    json_dic = {
      'tempereture': str(json_data['main']['temp']),
      'humidity': str(json_data['main']['humidity']),
      'weather': str(json_data['weather'][0]['description'])
    }
  return render(request, 'index.html', json_dic)