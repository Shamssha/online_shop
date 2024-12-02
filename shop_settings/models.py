from django.db import models

# Create your models here.
class Ttings(models.Model):
    phone = models.CharField(verbose_name="شماره موبایل", max_length=20)
    email = models.EmailField(verbose_name="آدرس ایمیل", max_length=254)
    address = models.CharField(verbose_name="آدرس", max_length=250)
    facebook = models.CharField(("فیسبوک"), max_length=100)
    insta = models.CharField(("انستاگرام"), max_length=100)
    twit = models.CharField(("تویتر"), max_length=100)
    linkedin = models.CharField(("لینکدن"), max_length=100)

    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'