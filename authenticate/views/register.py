from rest_framework.generics import CreateAPIView
from users.models import User
from authenticate.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    """
    API view to handle user registration.

    This view allows new users to register by submitting the required data.
    The data is validated using the RegisterSerializer, and upon success,
    a new user instance is created.
    """
    queryset = User
    serializer_class = RegisterSerializer