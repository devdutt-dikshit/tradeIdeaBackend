from django.urls import path
from post import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path('register/', views.userRegister),
    path('subscribe/<ideaId>/', views.subscribedByIdea),
    path('fetch-idea/', views.fetchTradeIdea),
    path('create-idea/', views.createTradeIdea),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
