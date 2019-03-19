from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .email import is_valid_email
from user_management.exceptions.user_not_found import UserNotFoundException
from user_management.exceptions.user_not_authenticated import UserNotAuthenticatedException
from user_management.exceptions.invalid_user_data import InvalidUserDataException
from user_management.exceptions.user_already_login import UserAlreadyLoginException

class UserManager():
    @staticmethod
    def register(user_data):
        """Register user with validation"""
        if not (UserManager.validate_user(user_data)):
            raise InvalidUserDataException()
        user = UserManager.validate_user(user_data)
        try:
            created_user = User.objects.create_user(username=user.get('username'),
                                email=user.get('email'),
                                password=user.get('password'))
            return created_user
        except:
            raise InvalidUserDataException(error_code=104)

    @staticmethod
    def validate_user(user_data):
        """Validate user data before saving"""

        if type(user_data) is dict:
            username,email,password = [user_data[k] for k in ('username', 'email','password')]
            if not (username) or not (email) or not(password):
                return False
            else:
                return {
                    'username': username,
                    'email': email,
                    'password': password
                }
        else:
            return False
    
    @staticmethod
    def signin(request):
        """Authenticate login request"""
        if request.user.is_authenticated:
            raise UserAlreadyLoginException()
        if request is None or request.POST is None:
            raise InvalidUserDataException()

        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        username = username_or_email
        if is_valid_email(username_or_email):
            UserModel = get_user_model()
            users = UserModel.objects.filter(email = username_or_email)
            if not users:
                raise UserNotFoundException()
            username = users[0].username
        user = authenticate(request = request, username=username, password=password)

        if user is None:
            raise UserNotAuthenticatedException()
        else:
            login(request, user)
            return True
