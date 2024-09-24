from django.urls import path

from users.apps import UserConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentCreateAPIview

app_name = UserConfig.name

urlpatterns = [
    path('obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pay/', PaymentCreateAPIview.as_view(), name='payment'),
]
