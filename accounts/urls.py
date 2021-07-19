from django.urls import path

from .views import AccountLoginForm, AccountLogoutView, AccountRegistrationView

app_name = 'accounts'

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginForm.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
]
