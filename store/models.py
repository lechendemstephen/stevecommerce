import decimal
from django.db import models # type: ignore

# Create your models here.

class Products(models.Model): 
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # type: ignore
    image = models.ImageField(upload_to='products/', )
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_sale = models.BooleanField(default=False)
    

    def __str__(self): 

        return self.name
    
    class Meta: 
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    # function to calculate discount price
    def discount_price(self): 
        percentage = 0.5
        price = self.price * decimal.Decimal(percentage)

        return round(price, 2)



class Category(models.Model): 
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self): 

        return self.name
    
    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
