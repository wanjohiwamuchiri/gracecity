from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import git_update, iam_index

urlpatterns = [
    path('', iam_index, name='iam_index' ),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('git_update/', git_update, name='git_update'),
]

