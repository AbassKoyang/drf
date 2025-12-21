from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validators.validate_title, validators.validate_title_no_hello, validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'content',
            'sale_price',
            'edit_url',
            'url'
        ]

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request');
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk" : obj.pk}, request=request)