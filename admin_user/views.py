
from rest_framework import status
from rest_framework.views import APIView

from . tokens import create_jwt_pair_for_user
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *

from rest_framework_simplejwt.tokens import RefreshToken
from . auth import CustomEmployeeAuthenticationBackend
from django.core.cache import cache

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Admin_User
from .serializers import AdminUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken




class LoginView(APIView):
    '''Login View'''
    permission_classes = []
    serializer_class = AdminSerializer

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        print(email, password)

        user = CustomEmployeeAuthenticationBackend.authenticate(self, request=request, email=email, password=password)


        if user is not None:
            # Set the user as active
            user.is_active = True
            user.save()

            # Perform further actions
            tokens = create_jwt_pair_for_user(user)

            user_serializer = self.serializer_class(user)
           

            response = {"message":"Logged in Sucessfully", 
                        "user": user_serializer.data,
                        "access": tokens.get('access'), 
                        "refresh" : tokens.get('refresh') }
            
           
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

  
    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)
    


User = get_user_model()

class LogoutView(APIView):
    """Used to blacklist token refresh and set user as inactive"""
    permission_classes = []

    def post(self, request: Request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            jti = token.payload['jti']
            user_id = token.payload['user_id']

            # Add the token to the blacklist
            outstanding_token = OutstandingToken.objects.get(jti=jti)
            BlacklistedToken.objects.create(token=outstanding_token)

            # Set user as inactive
            user = User.objects.get(id=user_id)
            user.is_active = False
            user.save()

            # Logout the user
            logout(request)

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = Admin_User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(is_staff=True)