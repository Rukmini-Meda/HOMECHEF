from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    imageFileName = models.CharField(max_length=30,default="profilepic4.png")
    email = models.EmailField(default="homechef302020@gmail.com")
    phone = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    address = models.TextField()
    timings = models.TextField(default="09AM - 06PM")
    food_items = models.ManyToManyField('FoodItem')
    
    def __str__(self):
        return self.name

    def food_list(self):
        return self.food_items.all()

class FoodItem(models.Model):
    itemname = models.CharField(max_length=30)
    imageFileName = models.CharField(max_length=30,default="food_img2.jpg")
    ingredients=models.ManyToManyField('Ingredients')
    description = models.TextField(max_length=100)
    vendors = models.ManyToManyField(Vendor)
    rating = models.IntegerField(default=3)
    def __str__(self):
        return self.itemname
    def vendor_list(self):
        return self.vendors.all()
    def ingred_lis(self):
        return self.ingredients.all()

class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
