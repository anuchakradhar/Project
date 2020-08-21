from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignUpForm, UserUpdateForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.
class UserRegisterView(SuccessMessageMixin, CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	success_message = "Your account was created successfully"

# class Profile(DetailView):
# 	template_name = 'registration/profile.html'

@login_required
def Profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated...')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = EditProfileForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'registration/profile.html', context)



# class UserEditView(UpdateView):
# 	form_class = UserChangeForm
# 	template_name = 'registration/edit_profile.html'
# 	success_url = reverse_lazy('home')
#
# 	def get_object(self):
# 		return self.request.user
