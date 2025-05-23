from rest_framework.generics import CreateAPIView
from users.models import User
from authenticate.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User
    serializer_class = RegisterSerializer