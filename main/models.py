from django.db import models
from autoslug import AutoSlugField
from .utils import slugify_fun


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation") 

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    slug = AutoSlugField(populate_from=slugify_fun, unique=True, editable=False)

    # slug = AutoSlugField(populate_from='name')

    # slug это путь продукта 
    # slug = models.SlugField(unique=True, max_length=100, verbose_name="Slug")

    image = models.ImageField(upload_to="products/", verbose_name="Image")
    name = models.CharField(max_length=100, verbose_name="Category name")
    description = models.TextField(max_length=500, verbose_name="Description")
    price = models.PositiveIntegerField(verbose_name="Price")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation") 
   
   
    def __str__(self):
        return f"{self.name} | {self.price} | {self.created_at}"
    
    class Meta: 
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(max_length=500, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Date of creation") 
   
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-created_at"]