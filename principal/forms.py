from django import forms
from users.models import User

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
# jean con este  formulario no puedo crear  usuarios
	email = forms.EmailField()



class UserFormxx(forms.ModelForm):
 # con este  si  puedo  crear  usuarios  solo quitale las xx  y renombra el  UserFor de UserCreationForm
	class Meta:
		model = User
		fields = ('username', 'email','password')
	

#class AuthorForm(forms.ModelForm):

#	class Meta:
#		model = User



class LoginForm(forms.Form):
	
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50,
		widget = forms.TextInput(attrs={ 'type' : 'password'
		}))