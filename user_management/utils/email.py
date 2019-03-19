from django.core.validators import validate_email, ValidationError

def is_valid_email(email):
    try:
        validate_email(email)
        valid_email = True
    except ValidationError:
        valid_email = False
    return valid_email