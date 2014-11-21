from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

from .forms import UserForm

#class IndexView(TemplateView):

#	template_name = 'index.html'

#class OtraUrlView(RedirectView):
#	url ='/'
 
class IndexView(FormView):

	form_class = LoginForm
	template_name = 'index.html'
	success_url = '/'

	def form_valid(self, form):
		user = authenticate(username = form.cleaned_data['username'],
				 password = form.cleaned_data['password'])
		if user is not None:
			if user.is_active:
				login(self.request, user)
		return super(IndexView, self).form_valid(form)

def LogOut(request):
	logout(request)
	return redirect('/')


class NuevoUsuario(FormView):
	
	form_class =  UserForm
	template_name = 'nuevousuario.html'
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		user.email = form.cleaned_data['email']
		user.save()
		return super(NuevoUsuario, self).form_valid(form)



