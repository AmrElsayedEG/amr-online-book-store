from authenticate.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(CreateAPIView):
    """
    API view to handle user login.

    This view validates the provided credentials using the LoginSerializer.
    On successful authentication, it returns a pair of JWT tokens (access and refresh),
    along with basic user information.

    Attributes:
        serializer_class (LoginSerializer): The serializer class used to validate user credentials.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.pk,
                'username' : user.username,
                'email' : user.email,
                'user_type' : user.get_user_type_display()
        }
        return Response(data, status=200)