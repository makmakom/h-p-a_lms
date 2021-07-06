from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView


class AccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


# class AccountLoginForm(LoginView):
#     pass
