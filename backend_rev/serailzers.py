from django.contrib.auth.models import User
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

class RegisterPassword(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            **validated_data
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(
        read_only=True
    )
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items =  OrderItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "created_at",
            "items"
        ]