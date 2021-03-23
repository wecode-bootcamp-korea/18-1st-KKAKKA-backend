import jwt

from django.http    import JsonResponse

from .models        import Account
from my_settings    import ALGORITHM, SECRET_KEY

def Validator(func):
    def Finder(self, request, *args, **kwargs):
        encoded_token = request.headers.get('Authorization')
    
        try:
            if encoded_token:
                decoded_token = jwt.decode(encoded_token, SECRET_KEY, ALGORITHM)
                request.pk    = Account.objects.get(id=decoded_token['id'])
            return JsonResponse({'message':'error_signin_needed'}, status=401)

        except Account.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=401)
    
    return Finder

