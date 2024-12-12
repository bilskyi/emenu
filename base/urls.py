from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantViewSet, MenuViewSet, MenuItemViewSet,
    TableViewSet, OrderViewSet, OrderDetailViewSet,
    MenuItemCategoryViewSet
)

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('menus', MenuViewSet)
router.register('menu-item-categories', MenuItemCategoryViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('tables', TableViewSet)
router.register('orders', OrderViewSet)
router.register('order-details', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
