import account
from .models import Address, Order, ProductCart, Status
from product.models import Product, OptionProduct
from account.validator import Validator

class ProductCartView(View):
    def post(self, request):
        try:
            data = json.load(request.body) 
        except: 
            
@Validator
class OrderView(View):
    def post(self, request):
        try:
            data = json.load(request.body)
            
            account = data['account']
            address = data['address']
            paymentmethod = data['payment']
            status = data['status']
        except: