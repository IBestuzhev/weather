from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(button_label='Register')
