import crypto
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

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


# def stockHome(request):
	# import requests
	# import json

	# api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_c7d75218621d4f8fb50eb8106dfbb90b")
  # api = json.loads(api_request.content)

  # return render(request, 'stockHome.html', {'api': api})

def stockHome(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" +
		                           ticker + "/quote?token=pk_c7d75218621d4f8fb50eb8106dfbb90b")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'stockHome.html', {'api': api})



	else:
		return render(request, 'stockHome.html', {'ticker': "Enter a Ticker Symbol Above..."})

  # pk_c7d75218621d4f8fb50eb8106dfbb90b

def about(request):
  return render(request, 'about.html', {})

def add_stock(request):
  if request.method == 'POST':
    form = StockForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ("Stock Has Been Added!"))
      return redirect('add_stock')
  ticker = Stock.objects.all()
  return render(request, 'add_stock.html', {'ticker': ticker})


# def add_stock(request):
# 	import requests
# 	import json

# 	if request.method == 'POST':
# 		form = StockForm(request.POST or None)

# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, ("Stock Has Been Added!"))
# 			return redirect('add_stock')

# 	else:
# 		ticker = Stock.objects.all()
# 		output = []
# 		for ticker_item in ticker:
# 		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(
#                     ticker_item) + "pk_c7d75218621d4f8fb50eb8106dfbb90b")
# 		try:
# 				api = json.loads(api_request.content)
# 				output.append(api)
# 			except Exception as e:
# 				api = "Error..."

# 		return render(request, 'add_stock', {'ticker': ticker, 'output': output})
