from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS
from .models import Restaurant, Menu, MenuItem, Table, Order, OrderDetail, MenuItemCategory
from .serializers import (
    RestaurantSerializer, MenuSerializer, MenuItemSerializer,
    TableSerializer, OrderSerializer, OrderDetailSerializer,
    MenuItemCategorySerializer,
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view restaurants
        return [IsAuthenticated()]  # Require authentication for create, update, delete


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view menus
        return [IsAuthenticated()]  # Require authentication for create, update, delete


class MenuItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuItemCategory.objects.all()
    serializer_class = MenuItemCategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view categories
        return [IsAuthenticated()]  # Require authentication for create, update, delete


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view menu items
        return [IsAuthenticated()]  # Require authentication for create, update, delete


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view tables
        return [IsAuthenticated()]  # Require authentication for create, update, delete


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view or create orders
        return [IsAuthenticated()]  # Require authentication for update, delete


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Allow unauthenticated users to view order details
        return [IsAuthenticated()]  # Require authentication for create, update, delete
