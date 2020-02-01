from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:register')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
