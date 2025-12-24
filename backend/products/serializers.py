from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validators.validate_title, validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'user',
            'my_user_data',
            'title',
            'price',
            'body',
            'sale_price',
            'edit_url',
            'url',
            'public'
        ]

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request');
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk" : obj.pk}, request=request)
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }