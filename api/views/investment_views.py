from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.investment import Investment
from ..serializers import InvestmentSerializer

class Investments(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvestmentSerializer
    def get(self, request):
        """Index request"""
        investments = Investment.objects.filter(owner=request.user.id)
        data = InvestmentSerializer(investments, many=True).data
        return Response({ 'investments': data })

    def post(self, request):
        """Create request"""
        request.data['investment']['owner'] = request.user.id
        investment = InvestmentSerializer(data=request.data['investment'])
        if investment.is_valid():
            investment.save()
            return Response({ 'investment': investment.data }, status=status.HTTP_201_CREATED)
        return Response(investment.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        investment = get_object_or_404(Investment, pk=pk)
        if request.user != investment.owner:
            raise PermissionDenied('Unauthorized, you do not own this investment')
        data = InvestmentSerializer(investment).data
        return Response({ 'investment': data })

    def delete(self, request, pk):
        """Delete request"""
        investment = get_object_or_404(Investment, pk=pk)
        if request.user != investment.owner:
            raise PermissionDenied('Unauthorized, you do not own this investment')
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        investment = get_object_or_404(Investment, pk=pk)
        if request.user != investment.owner:
            raise PermissionDenied('Unauthorized, you do not own this investment')

        request.data['investment']['owner'] = request.user.id
        data = InvestmentSerializer(investment, data=request.data['investment'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
