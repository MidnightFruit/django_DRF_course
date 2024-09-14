from django.urls import path

from users.apps import UserConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UserConfig.name

urlpatterns = [
    path('obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
