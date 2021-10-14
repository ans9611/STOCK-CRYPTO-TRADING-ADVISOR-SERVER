from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.investment import Investment
from ..serializers import InvestmentSerializer

# Create your views here.
class Investments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = InvestmentSerializer
    def get(self, request):
        """Index request"""
        investments = Investment.objects.filter(account=request.user.id)
        data = InvestmentSerializer(investments, many=True).data
        return Response({ 'investments': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['investment']['account'] = request.user.id
        # Serialize/create investment
        investment = InvestmentSerializer(data=request.data['investment'])
        # If the investment data is valid according to our serializer...
        if investment.is_valid():
            # Save the created investment & send a response
            investment.save()
            return Response({ 'investment': investment.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(investment.errors, status=status.HTTP_400_BAD_REQUEST)

class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        investment = get_object_or_404(Investment, pk=pk)
        if request.user != investment.account:
            raise PermissionDenied('Unauthorized, you do not own this investment')

        data = InvestmentSerializer(investment).data
        return Response({ 'investment': data })

    def delete(self, request, pk):
        """Delete request"""
        investment = get_object_or_404(Investment, pk=pk)
        if request.user != investment.account:
            raise PermissionDenied('Unauthorized, you do not own this investment')
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Investment
        # get_object_or_404 returns a object representation of our Investment
        investment = get_object_or_404(Investment, pk=pk)
        # Check the investment's account against the user making this request
        if request.user != investment.account:
            raise PermissionDenied('Unauthorized, you do not own this investment')

        # Ensure the account field is set to the current user's ID
        request.data['investment']['account'] = request.user.id
        # Validate updates with serializer
        data = InvestmentSerializer(investment, data=request.data['investment'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
