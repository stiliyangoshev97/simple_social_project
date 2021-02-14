from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	class Meta():
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

		def __init__(self, *args, **kwargs):
			# When the user comes in and it's ready to sign up
			# We are going to call the UserCreationForm
			# and he will have access to the fields above
			super().__init__(*args, **kwargs)
			# Set up the label for the actual field
			self.fields['username'].label = 'Display Name'
			self.fields['email'].label = "Email Address"