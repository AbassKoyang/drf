from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data 
        return Response(data);
    return Response({'message': "Invalid data"}, status=400)