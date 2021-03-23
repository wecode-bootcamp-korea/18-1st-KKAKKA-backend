from account.validator import Validator
import json,bcrypt,jwt,re
from json.decoder     import JSONDecodeError

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse

from .models          import Account
from my_settings      import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            name          = data['name']
            email         = data['email']
            phone_number  = data['phone']
            password      = data['password']

            account_check = Account.objects.filter(Q(email=email) | Q(phone_number=phone_number)).exists()
            email_check   = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

            if email_check.match(email) is None:
                return JsonResponse({'message':'error_email_form'}, status=401)            

            if len(password)<8: 
                return JsonResponse({'message':'error_password_form'}, status=401)     

            if account_check:
                return JsonResponse({'message':'error_signup_already'}, status = 401)           

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_password= hashed_password.decode('utf-8')
            Account.objects.create(email=email, name=name, phone_number=phone_number, password=decoded_password)
            return JsonResponse({'message':'success_signup'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)            

        except JSONDecodeError:
            return JsonResponse({'message': 'JSONDecodeError'}, status=400)   


class SignInView(View):
    def post(self, request):
        try:    
            data          = json.loads(request.body)
            id            = data['id']
            password      = data['password']
            account_check = Account.objects.get(Q(email=id) | Q(phone_number=id))

            if account_check:
                decoded_password = account_check.password.encode('utf-8')
                encoded_password = password.encode('utf-8')
                if bcrypt.checkpw(encoded_password, decoded_password):
                    token = jwt.encode({'id':account_check.id}, SECRET_KEY, ALGORITHM)
                    return JsonResponse({'message':'success_signin', 'access_token':token}, status=201)
                return JsonResponse({'message':'error_password_matching'}, status = 401)

        except Account.MultipleObjectsReturned:
            return JsonResponse({'message': 'error_mutiple_id'}, status=401)

        except Account.DoesNotExist:
            return JsonResponse({'message': 'error_no_id'}, status=401)            

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)            

        except JSONDecodeError:
            return JsonResponse({'message': 'JSONDecodeError'}, status=400)  

