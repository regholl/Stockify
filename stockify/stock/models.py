from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StockDeposit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    user_balance = models.DecimalField(max_digits=10,decimal_places=2,default=10000.00)

    def __str__(self):
        return f'{self.user.username} - {self.stock_name}'
    

