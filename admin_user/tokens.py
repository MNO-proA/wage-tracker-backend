from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from . models import Admin_User


User = get_user_model()


def create_jwt_pair_for_user(user: User): # type: ignore
    refresh = RefreshToken.for_user(user)

    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}

    return tokens


def verify_and_get_user_from_request(request):
    access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

    try:
        token = AccessToken(access_token)
        # Verify the token's signature and expiration
        token.verify()
        # Retrieve the user ID from the token's payload
        user_id = token.payload["id"]
        # Retrieve the user object using the user_id
        user = Admin_User.objects.get(pk=user_id)
        return user
    except (TokenError, User.DoesNotExist):
        # Token is invalid or expired, or user does not exist
        return None
