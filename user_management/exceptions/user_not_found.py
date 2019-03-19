from django.utils.translation import gettext as _

class UserNotFoundException(BaseException):
    error_code = 101
    message = _('User Not Found')
