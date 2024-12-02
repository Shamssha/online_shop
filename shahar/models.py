from django.db import models 
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Product(models.Model):
    pr_name = models.CharField(("نام محصول"), max_length=50)
    pr_discription = models.CharField(("توضیحات محصول"), max_length=200)
    pr_price = models.IntegerField(("قیمت"))
    pr_catagory = models.ForeignKey("Catagory", verbose_name=("دسته بندی"), on_delete=models.CASCADE)
    pr_photo = models.ImageField(("تصویر"), upload_to='photo/', height_field=None, width_field=None, max_length=None)
    SIZE = (
        ('m',32),
        ('L',42),
        ('XL',52)
    )
    pr_size = models.CharField(("اندازه"), max_length=5,choices=SIZE,default=32)
    pr_is_sale = models.BooleanField(("فروش ویژه"),default=False)
    pr_sale_price = models.IntegerField(("قیمت تخفیف"),default=0)
    star = models.IntegerField(("ستاره"),validators=[MaxValueValidator(5),MinValueValidator(0)])
    pr_brand = models.ManyToManyField("Brand", verbose_name=("برند"),related_name="brands")
    pr_color = models.ManyToManyField("Color", verbose_name=("رنگ"))
    def __str__(self):
        return self.pr_name
    class Meta:
        verbose_name = 'جدول محصولات'
        verbose_name_plural = 'محصولات'
        
    
class Catagory(models.Model):
    name = models.CharField(("دسته بندی"), max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'جدول دسته بندی ها'
        verbose_name_plural = 'دسته بندی '
    
class Brand(models.Model):
    brand_name =models.CharField(("نام برند"), max_length=50)
    brand_photo= models.ImageField(("تصویر"), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.brand_name
    class Meta:
        verbose_name = 'جدول برند'
        verbose_name_plural = 'برند'

    
class Color(models.Model):
    color = models.CharField(("رنگ"), max_length=50)

    def __str__(self):
        return self.color
    class Meta:
        verbose_name = 'جدول رنگ ها'
        verbose_name_plural = 'رنگ ها'

class ProductGalary(models.Model):
    product = models.ForeignKey(Product,verbose_name='محصول',on_delete=models.CASCADE)
    image = models.ImageField(("تصویر"), upload_to='galary/', height_field=None, width_field=None, max_length=None)
    name = models.CharField(("نام"), max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'
    
class ProductManager(models.Manager):
    pass