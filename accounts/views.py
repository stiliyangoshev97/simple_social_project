from django.shortcuts import render
# We use this inn case somebody is logged in, 
# where should he actually go
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

# Create your views here.
class SignUp(CreateView):
	form_class = forms.UserCreateForm
	# Once someone signs up, he will go back to the login page
	# We use reverse_lazy so he won't be redirected if he doesn't
	# Sign-up successfully
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

