from django.utils.translation import gettext as _

class UserAlreadyLoginException(BaseException):
    error_code = 105
    message = _('User is already authenticated. Please logout first.')