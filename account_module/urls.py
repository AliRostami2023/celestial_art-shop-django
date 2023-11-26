from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path('forget-pass/', views.ForgetPassView.as_view(), name='forget-pass-page'),
    path('reset-pass/<active_code>/', views.ResetPassView.as_view(), name='reset-pass-page'),
    path('active-account/<email_active_code>/', views.ActivateAcountView.as_view(), name='active-account-page'),
]
