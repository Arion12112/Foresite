from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView, View
from .forms import SignUpForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

        return render(request, self.template_name, {'form': form})
