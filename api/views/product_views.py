from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.product import Product
from ..serializers import ProductSerializer

# Create your views here.
class Products(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ProductSerializer
    def get(self, request):
        """Index request"""
        # Get all the products:
        # products = Product.objects.all()
        # Filter the products by owner, so you can only see your owned products
        products = Product.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ProductSerializer(products, many=True).data
        return Response({ 'products': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['product']['owner'] = request.user.id
        # Serialize/create product
        product = ProductSerializer(data=request.data['product'])
        # If the product data is valid according to our serializer...
        if product.is_valid():
            # Save the created product & send a response
            product.save()
            return Response({ 'product': product.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the product to show
        product = get_object_or_404(Product, pk=pk)
        # Only want to show owned products?
        if request.user != product.owner:
            raise PermissionDenied('Unauthorized, you do not own this product')

        # Run the data through the serializer so it's formatted
        data = ProductSerializer(product).data
        return Response({ 'product': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate product to delete
        product = get_object_or_404(Product, pk=pk)
        # Check the product's owner against the user making this request
        if request.user != product.owner:
            raise PermissionDenied('Unauthorized, you do not own this product')
        # Only delete if the user owns the  product
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Product
        # get_object_or_404 returns a object representation of our Product
        product = get_object_or_404(Product, pk=pk)
        # Check the product's owner against the user making this request
        if request.user != product.owner:
            raise PermissionDenied('Unauthorized, you do not own this product')

        # Ensure the owner field is set to the current user's ID
        request.data['product']['owner'] = request.user.id
        # Validate updates with serializer
        data = ProductSerializer(product, data=request.data['product'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
