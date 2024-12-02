from django.contrib import admin

from shahar import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'pr_price', 'pr_sale_price', 'star', 'pr_catagory', 'pr_size']
    
    class Meta:
        model = models.Product


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Catagory)
admin.site.register(models.Brand)
admin.site.register(models.Color)
admin.site.register(models.ProductGalary)

