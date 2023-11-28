from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'categories'
        

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    productname = models.CharField(max_length=200)
    quantity = models.IntegerField(default='0', blank=False, null=False)
    receive_quantity = models.IntegerField(default='0', blank=False, null=True)
    receive_by =models.CharField(max_length=50, blank=False,null=False)
    issue_quantity = models.IntegerField(default='0', blank=False, null=True)
    issue_to = models.CharField(max_length=200, blank=False,null=False)
    issue_by =models.CharField(max_length=50, blank=False,null=False)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.productname


class ProductHistory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    created = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
 
    class Meta:
        ordering = ['-updated', '-created']
    
   
 
    

        
    