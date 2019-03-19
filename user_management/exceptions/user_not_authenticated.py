from django.utils.translation import gettext as _

class UserNotAuthenticatedException(BaseException):
    error_code = 102
    message = _('User is not authenticated')