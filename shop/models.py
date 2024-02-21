from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                               related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


COLOR_CHOICES = [
    ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'),
    ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'),
    ('black', 'Black'), ('white', 'White'), ('gray', 'Gray'), ('cyan', 'Cyan'),
    ('magenta', 'Magenta'), ('teal', 'Teal'), ('olive', 'Olive'), ('lime', 'Lime'),
    ('navy', 'Navy'), ('maroon', 'Maroon'), ('silver', 'Silver'), ('gold', 'Gold'),
]

SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', '2 Extra Large'),
]


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    quantity = models.PositiveIntegerField(default=0)  # Quantity of the product available
    colours = models.ManyToManyField('Colour', choices=COLOR_CHOICES,
                                     related_name='products')  # Many-to-many relationship with Colour model
    sizes = models.ManyToManyField('Size', choices=SIZE_CHOICES,
                                   related_name='products')  # Many-to-many relationship with Size model

    def __str__(self):
        return self.name


def product_image_path(instance, filename):
    product_name = instance.Product.name
    category_name = instance.Product.category.name
    product_slug = slugify(product_name)
    category_slug = slugify(category_name)
    return f'product_images/{category_slug}/{product_slug}/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path)

    def __str__(self):
        return f'Image for {self.product.name}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_items = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateTimeField(default=timezone.now)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return f'Order #{self.pk}'
