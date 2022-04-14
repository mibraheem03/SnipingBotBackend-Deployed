from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet, BotViewSet, ComissionViewSet
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'auth/bot', BotViewSet, basename='bot')
routes.register(r'auth/comission', ComissionViewSet, basename='comission')
# USER
routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls

]
