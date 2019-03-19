from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as logoutAction
from django.http import JsonResponse
from .utils.user_manager import UserManager
import json

@csrf_exempt
@require_http_methods(['POST'])
def register(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'error': True,
            'message': 'Already logged in.'
        }, status=401)
    else:
        UserManager.register(user_data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        })
        return JsonResponse({
            'error': False
        })

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    is_authenticated = UserManager.signin(request)
    return JsonResponse({
        'error': not is_authenticated
    })

@csrf_exempt
@require_http_methods(['GET'])
def logout(request):
    is_sucessful = False
    try:
        logoutAction(request)
        is_sucessful = True
    except: 
        is_sucessful = False
    
    return JsonResponse({
        'error': not is_sucessful
    })