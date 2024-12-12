from rest_framework import serializers
from .models import (
    Restaurant,Menu,
    MenuItem, Table,
    Order, OrderDetail,
    MenuItemCategory,
    )


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItemCategory
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    category = MenuItemCategorySerializer()

    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Table
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
