from django.urls import path
from .views.investment_views import Investments, InvestmentDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    path('investments/', Investments.as_view(), name='investments'),
    path('investments/<int:pk>/', InvestmentDetail.as_view(), name='investment_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
