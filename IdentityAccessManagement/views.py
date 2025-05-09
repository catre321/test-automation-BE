from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    """
    Get details of the currently authenticated user
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    @swagger_auto_schema(
        operation_summary="Get current user details",
        operation_description="Retrieve information about the currently authenticated user. Add 'Bearer {token}' to the Authorization header.",
        responses={
            200: UserSerializer,
            401: "Authentication credentials were not provided"
        },
        security=[{'Bearer': []}],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Bearer {token}",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_object(self):
        return self.request.user
    
# class LogoutView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"success": "Logged out successfully"})
#         except Exception:
#             return Response({"error": "Invalid token"}, status=400)
