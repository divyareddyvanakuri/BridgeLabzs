from django.shortcuts import render
from .serializer import RegisterSerializer, LoginSerializer,PasswordResetSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate,get_user_model
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.template.loader import render_to_string
from chatapp.token import create_auth_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.context_processors import csrf
from chatapp.token import create_auth_token
import jwt

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
#from rest_framework.authtoken import au


# Create your views here.


class LoginApiView(APIView):
    serialzer_class = LoginSerializer

    def get(self, request):
        return render(request, 'Loginpage.html')

    def post(self, request):
        # authentication_classes = [SessionAuthentication, BasicAuthentication]
        # permission_classes = [IsAuthenticated]
        data = request.data 
        username = data.get('username')
        print(username)
        password = data.get('password')
        print(password)
        user = authenticate(username=username,password=password)
        queryset = User.objects.filter(username=username, password=password).count()
        if queryset == 0:
            return HttpResponse("user is not active")
        return render(request,'index.html')

class RegisterApiView(APIView):
    

    def get(self, request):
        return render(request, 'registerationpage.html')

    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirmpassword = data.get('confirmpassword')

        if password == confirmpassword:
            user = User.objects.create(
                username=username, email=email, password=password)
            user.save()
            current_site = get_current_site(request)
            domain = current_site.domain
            token = create_auth_token(user)
            url = str(token)
            surl = get_surl(url)
            z = surl.split('/')

            print("short_url", z[2])
            subject = "please active your account"
            msg = render_to_string('email_validation.html', {
                'user': user.username,
                'domain': domain,
                'surl': z[2]
            })
            to_email = email
            mail = EmailMessage(subject, msg, to=[to_email])
            mail.send()
        print(msg)
        return HttpResponse("Thanks for Registation,please Activate your Account through mailed link")


def activate(request, surl):   
    print("surl :", surl)
    return render(request,'Loginpage.html')


class PasswordResetApiView(APIView):
    serializer_class = PasswordResetSerializer
    #permission_classes  = (AllowAny,)
    def get(self,request):
        return render(request,'resetpassword.html')
    def post(self,request):
        data = request.data
        email = data.get('email')
        #user = authenticate(username=username,password=password)
        queryset = User.objects.filter(email=email).count()
        if queryset == 0:
            return HttpResponse("user is not active")
        else:
            q = User.objects.get(email=email)
            print(q.email)
            print(q.username)
            print(q.password)
            user = {}
            user[user.username]=q.username
            user[user.password]=q.password
            current_site = get_current_site(request)
            domain = current_site.domain
            token = create_auth_token(user)
            url = str(token)
            surl = get_surl(url)
            z = surl.split('/')
            print("short_url", z[2])
            subject = "please reset your account"
            msg = render_to_string('password_validation.html', {
                'user': user.username,
                'domain': domain,
                'surl': z[2]
            })
            to_email = q.email
            mail = EmailMessage(subject, msg, to=[to_email])
            mail.send()
            print(msg)
            return HttpResponse("please confirm your reset password")
            

