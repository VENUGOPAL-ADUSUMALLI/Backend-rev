from rest_framework import  serializers
from  .models import  *

class ProductSerializer(serializers.ModelSerializer):

    display_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'is_available', 'display_name']
        read_only_fields = ["id"]
    def validate_price(self, value):
        if value < 100:
            raise serializers.ValidationError(
                "price must be greater that 100"
            )
        return  value

    def get_display_name(self, obj):
        return  f" ₹{obj.price}"