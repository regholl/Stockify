from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from . models import StockDeposit
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from . import utils
from . import utils
# Create your views here.

def stock_fetch(request):
    symbols = ['AAPL','AMZN','META','MSFT','ABNB','ADBE','PFE','ASTR','TSLA','AAL']
    data = utils.stock_fetch_api(symbols)
    context = {'data':data} 

    return render(request,'stock/stocktable.html',context)

@login_required
def buy_stock(request):
    if request.method =='POST':
        stock_name = request.POST.get('stock_name')
        amount = request.POST.get('amount')
        
        unit_price = utils.unit_price_fetch(stock_name)
        total_price = unit_price*amount
        stock_deposit =StockDeposit(user =request.user,
                                    stock_name = stock_name,
                                    amount = amount,
                                    unit_price =unit_price,
                                    total_price =total_price,
                                    user_balance = 0)
        user = request.user
        current_balance = user.stock_deposit.user_balance
        updated_balance = current_balance -total_price

        user.stock_deposit.user_balance = updated_balance
        user.stock_deposit.save()

        stock_deposit.save()
        messages.success('Successfully Purchashed!')
        return render('buy_stock')

    return render(request,'stock/buy_stock.html')
    

    



    

   

    



