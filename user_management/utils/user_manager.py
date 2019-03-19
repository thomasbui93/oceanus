from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class UserManager():
    @staticmethod
    def register(user_data):
        """Register user with validation"""
        if not (UserManager.validate_user(user_data)):
            return False
        user = UserManager.validate_user(user_data)
        return User.objects.create_user(username=user.get('username'),
                                email=user.get('email'),
                                password=user.get('password'))

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
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request = request, username=username_or_email, password=password)
        if user is None:
            return False
        else:
            login(request, user)
            return True
