from django.contrib.auth.models import User
from django.db import models

from shahar.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(("پرداخت شده/ نشده"), default=False)
    pay_date = models.DateTimeField(("تاریخ پرداخت"), blank=True, auto_now_add=True)
    
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.user.get_full_name()
    
class OrderDetail(models.Model):
    order =models.ForeignKey(Order, verbose_name=("سفارش"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("محصول"), on_delete=models.CASCADE)
    count = models.IntegerField(("مقدار"))
    price = models.IntegerField(("قیمت"))

    class Meta:
        verbose_name = 'جزئیات'
        verbose_name_plural = 'جزئیات'

    def __str__(self) -> str:
        return self.product.pr_name
