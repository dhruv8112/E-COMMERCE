from django.db import models
from django.utils.html import format_html

# Create your models here.


class category(models.Model):
    cat_name = models.CharField(max_length=10)
    cat_img = models.ImageField(upload_to="categories")
    def img_return(self):
     return format_html('<img src="/media/{}" style="width:30px;height:30px"/>'.format(self.cat_img)) 



class product(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_title=models.CharField(max_length=10, default="Default")
    pro_cat = models.ForeignKey(
        category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()


class productImage(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product_images")
    img = models.ImageField(upload_to="products")
    def img2_return(self):
     return format_html('<img src="/media/{}"style="width:30px;height:30px"/>'.format(self.img)) 

