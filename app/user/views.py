from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    "Create new user in the ststem"
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES