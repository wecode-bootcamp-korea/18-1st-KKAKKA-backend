import json,jwt,bcrypt
from json.decoder     import JSONDecodeError

from django.views     import View
from django.http      import JsonResponse

from .models           import Address, Order
from account.validator import Validator
from account.models    import AdditionalInformation, Account

class AddressView(View):
    @Validator
    def post(self, request):
        try:    
            data            = json.loads(request.body)
            recipient_phone = data['recipient_phone']
            postal_code     = data['postal_code']
            recipient       = data['recipient']
            address         = data['address']
            sender          = data['sender']
            save_option     = data['save']

            # print(AdditionalInformation.objects.get(account_id=1))
        
            # # if AdditionalInformation.objects.get(account=request.pk).address is address: 
            # #     return JsonResponse({'message':'error_address_exist'}, status=401)

            Address.objects.create(sender=sender, recipient=recipient,recipient_phone_number=recipient_phone, postal_code=postal_code, address=address, save_option=save_option)
            return JsonResponse({'message':'success_address_input'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)            

        except JSONDecodeError:
            return JsonResponse({'message': 'JSONDecodeError'}, status=400) 
