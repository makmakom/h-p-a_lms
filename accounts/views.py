from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accounts.forms import AccountRegistrationForm


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegistrationForm


class AccountLoginForm(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('index')


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
