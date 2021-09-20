from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name="prices"),
    path('stockHome/', views.stockHome, name="stockHome"),
    path('about/', views.about, name="about"),
    path('add_stock/', views.add_stock, name="add_stock"),
    # pk_c7d75218621d4f8fb50eb8106dfbb90b
]
