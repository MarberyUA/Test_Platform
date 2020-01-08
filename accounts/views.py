from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from .forms import UserDetailUpdateForm
from django.views.generic import CreateView, UpdateView
from django.views import View
from .models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .forms import CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_toke
from django.core.mail import send_mail
from Test_Platform.settings import DEFAULT_FROM_EMAIL


# Create your views here.


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

    def post(self, request, *args, **kwargs):

        self.current_site = get_current_site(request)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        token = account_activation_toke.make_token(user)
        mail_subject = 'Activate your account.'
        message = 'The link for activation: ' + str(self.current_site) + '/accounts/activate/' + \
                  str(user.id) + '/' + str(token)
        to_email = form.cleaned_data.get('email')
        mail = send_mail(mail_subject, message, DEFAULT_FROM_EMAIL, [to_email])
        return redirect('login')


def activate(request, id, token):
    try:
        user = User.objects.get(id=id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_toke.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'account_activate.html', context={'success': 'You have registered successfully!', 'user': user})
    else:
        return render(request, 'account_activate.html', context={'error': 'Activation link is invalid', 'user': user})


class EmailResend(View):
    def post(self, request, id):
        user = User.objects.get(id=id)
        token = account_activation_toke.make_token(user)
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = 'The link for activation: ' + str(current_site) + '/accounts/activate/' + \
                  str(user.id) + '/' + str(token)
        to_email = user.email
        mail = send_mail(mail_subject, message, DEFAULT_FROM_EMAIL, [to_email])
        return render(request, 'account_activate_resend.html', context={'success': 'The activation link has been resent'})


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