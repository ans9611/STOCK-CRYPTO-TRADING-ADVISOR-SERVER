from django.shortcuts import render

# Create your views here.
def home(request):
  import requests
  import json
  api_request = requests.get(
      "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
  api = json.loads(api_request.content)
  # api dictionary
  return render(request, 'home.html', {'api': api})
