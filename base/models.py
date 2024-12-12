from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('MenuItemCategory', on_delete=models.CASCADE, related_name='categories')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return f"{self.name} - {self.menu.name}"


class MenuItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.CharField(max_length=10)
    qr_code = models.TextField(unique=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')

    def __str__(self):
        return f"Table {self.table_number} ({self.restaurant.name})"


class Order(models.Model):
    table = models.OneToOneField(Table, on_delete=models.CASCADE, related_name='order')
    datetime = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')

    def __str__(self):
        return f"Order {self.id} - Table {self.table.table_number}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order {self.order.id})"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.menu_item.price
        super().save(*args, **kwargs)
