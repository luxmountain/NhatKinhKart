from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=2100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])
        
    def __str__(self) -> str:
        return self.category_name