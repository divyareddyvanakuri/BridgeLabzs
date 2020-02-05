import jwt
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import csrf

# json web token activation
def create_auth_token(user):
    payload = {'username': user.username,
               'password': user.password}
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token
