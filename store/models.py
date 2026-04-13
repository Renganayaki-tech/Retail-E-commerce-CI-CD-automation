from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    badge = models.CharField(max_length=50, blank=True)

    image = models.URLField()
    
    image2 = models.URLField(blank=True)
    
    image3 = models.URLField(blank=True)

    description = models.TextField()

    material = models.CharField(max_length=200, blank=True)
    
    origin = models.CharField(max_length=200, blank=True)
    
    warranty = models.CharField(max_length=100, blank=True)

    stock = models.IntegerField(default=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()

    address = models.TextField()
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email