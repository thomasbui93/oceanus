from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as logoutAction
from django.http import JsonResponse
import json
from django.utils.translation import gettext as _
from .utils.user_manager import UserManager
from .exceptions.user_not_found import UserNotFoundException
from .exceptions.user_not_authenticated import UserNotAuthenticatedException
from .exceptions.invalid_user_data import InvalidUserDataException
from .exceptions.user_already_login import UserAlreadyLoginException

@csrf_exempt
@require_http_methods(['POST'])
def register(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'error': True,
            'message': UserAlreadyLoginException.message,
            'code': UserAlreadyLoginException.error_code
        }, status=401)
    else:
        try:
            UserManager.register(user_data = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
            })
            return JsonResponse({
                'error': False
            })
        except InvalidUserDataException:
            return JsonResponse({
                'error': True,
                'code': InvalidUserDataException.error_code,
                'message': InvalidUserDataException.message
            })

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    try:
        UserManager.signin(request)
        return JsonResponse({
            'error': False
        })
    except UserNotFoundException:
        return JsonResponse({
            'error': True,
            'message': UserNotFoundException.message,
            'code': UserNotFoundException.error_code
        })
    except UserNotAuthenticatedException:
        return JsonResponse({
            'error': True,
            'message': UserNotAuthenticatedException.message,
            'code': UserNotAuthenticatedException.error_code
        })
    except UserAlreadyLoginException:
        return JsonResponse({
            'error': True,
            'message': UserAlreadyLoginException.message,
            'code': UserAlreadyLoginException.error_code
        })
    finally:
        return JsonResponse({
            'error': True,
            'message': _('Unknown error!')
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