from django.shortcuts import render
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from .token import generate_token
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class Signup(APIView):
    def post(self,request):
        username=request.data.get('username')
        print(username)
        email=request.data.get('email')
        print(email)

        password=request.data.get('password')

        
        phone=request.data.get('phone')
        print(phone)


        if User.objects.filter(username=username).exists():

            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        

        myuser=User.objects.create_user(username=username,password=password,email=email)
        myuser.is_active = False
        myuser.save()

        curent_site=get_current_site(request)
        email_subject = 'confirmatiom mail @ PIXEL HUB'
        message2=render_to_string('activation_mail.html',{
            'name':myuser.username,
            'domain':curent_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently=True
        email.send()
        print("mail sent")
        return Response({'message' : 'user craeted successfully'},status=status.HTTP_201_CREATED)


def activate(request,uid64,token):
    try:
        uid= force_str(urlsafe_base64_decode(uid64))
        myuser=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        return HttpResponseRedirect(settings.SITE_URL_AUTH)
    else:
        return render(request,'authentication/activation_failed.html')


class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")  # Use get to avoid KeyError
            if not refresh_token:
                return Response({"error": "refresh_token not provided"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)

            if not token.token:
                return Response({"error": "Invalid refresh_token"}, status=status.HTTP_400_BAD_REQUEST)

            
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ResultAPIView(APIView):
    def post(self, request):
        username=request.data.get('username')
        score=request.data.get('correctOptionCount')
        print(username)
        print(score)
        myuser=User.objects.get(username=username)

        email_subject = 'Result of Quiz'
        message2=render_to_string('resultmail.html',{
            'name':username,
            'score':score
        })
        email = EmailMessage(
            email_subject,message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently=True
        email.send()
        return Response({'message': 'Data received successfully'}, status=status.HTTP_200_OK)
