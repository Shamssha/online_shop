from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(("نام"), max_length=100)
    email = models.EmailField(("ایمیل"), max_length=100)
    message = models.TextField(("پیام"))
    date = models.DateTimeField(("تاریخ"), auto_now_add=True)

    class Meta:
        verbose_name ='پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.name
    