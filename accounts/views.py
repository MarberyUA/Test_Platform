from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import reverse_lazy
from .forms import UserDetailUpdateForm
from django.views.generic import CreateView, UpdateView
from django.views import View
from .models import User
from Test.models import TestMarks, Test
from .forms import CustomUserCreationForm
from datetime import date


# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'


class UserDetail(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'accounts/account_details.html', context={'user': user})


class UserDetailUpdate(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = UserDetailUpdateForm(instance=user)
        return render(request, template_name='accounts/account_details_update.html', context={'user': user, 'form': form})

    def post(self, request, id):
        user = User.objects.get(id=id)
        form = UserDetailUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            new_obj = form.save()
            new_obj.birthday = request.POST.get('birthday', None)
            new_obj.save()
            return redirect(reverse('user_detail_url', kwargs={'id': user.id}))
        return redirect('main_page_url')


class ChangeUserDetails(UpdateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_reset_form.html.html'


class ChangeUserDetailsDone(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'