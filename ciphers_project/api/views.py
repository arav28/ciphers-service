from django.http import JsonResponse
from .ciphers import caesar_encode
# Create your views here.
def greetings(request):
    result = {"message":"welcome to ciphers service!"}
    return JsonResponse(result)

def encode(request,plaintext,shift):
    params= dict(request.GET)
    print(params)
    cipher = caesar_encode(plaintext,shift)
    return JsonResponse({"cipher":cipher})