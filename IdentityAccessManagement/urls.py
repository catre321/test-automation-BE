from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, UserDetailView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('register/', RegisterView.as_view(), name='register'), # All user-personell register is through superadmin in Django Admin
    path('user/', UserDetailView.as_view(), name='user_detail'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]