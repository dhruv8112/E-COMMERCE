from django.contrib import admin
from .models import category, product, productImage
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=('cat_name','img_return',)

class productAdmin(admin.ModelAdmin):
    list_display=('pro_title','pro_name','price',)

class ImgAdmin(admin.ModelAdmin):
    list_display=('product','img2_return',)

 


admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)
admin.site.register(productImage,ImgAdmin)