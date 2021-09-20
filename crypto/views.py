import crypto
from django.shortcuts import render

# Create your views here.
def home(request):
  import requests
  import json

  price_request = requests.get(
      "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,DOGE,SHIB,ETH,XRP,SOL&tsyms=USD")
  price = json.loads(price_request.content)


  api_request = requests.get(
      "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
  api = json.loads(api_request.content)
  # api dictionary
  return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
  if request.method == 'POST':
    import requests
    import json
    # send request to post to prices.html
    quote = request.POST['quote']
    # converts to upper case to search so allows to search lower or uppercase name of the quote
    quote = quote.upper()
    # request selected name of crypto
    crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
    crypto = json.loads(crypto_request.content)
    return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})

# Error handler
  else:
    notfound = "Enter a CORRECT crypto currency symbol into the form above..."
    return render(request, 'prices.html', {'notfound': notfound})
