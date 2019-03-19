from django.utils.translation import gettext as _

class InvalidUserDataException(BaseException):
    error_code = 103
    message = _('Invalid user data.')

    def __init__(self, error_code = 103):
        self.error_code = error_code
        self.message = self.getMessage()

    def getMessage(self):
        if self.error_code == 103:
            return _('Invalid user data.')
        else:
            return _('Error while create user data.')