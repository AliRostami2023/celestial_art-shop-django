from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account_module.forms import RegisterForm, LoginForm, ForgetPassForm, ResetPassForm
from account_module.models import User
from utils.email_service import send_email


# Create your views here.


class RegisterView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                username=user_email, first_name=first_name, last_name=last_name)
                new_user.set_password(user_password)
                new_user.save()
                messages.success(request, 'برای فعالسازی حساب کاربری ایمیل خود را چک کنید')
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/verify-user.html')
                return redirect(reverse('register-page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAcountView(View):
    def get(self, request: HttpRequest, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo:show message success to user
                return redirect(reverse('login-page'))
            else:
                # todo:show message activate account
                pass

        raise Http404


class LoginView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری فعال نشده است')

                else:
                    is_password_currect = user.check_password(user_password)
                    if is_password_currect:
                        login(request, user)

                        if request.user.is_superuser:
                            return redirect(reverse('dashboard-page'))
                        else:
                            return redirect(reverse('dashboard-user-page'))
                    else:
                        login_form.add_error('password', 'کلمه عبور اشتباه است')

            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgetPassView(View):
    def get(self, request: HttpRequest):
        forget_pass = ForgetPassForm()
        context = {
            'forget_pass': forget_pass
        }
        return render(request, 'account_module/forget-pass.html', context)

    def post(self, request: HttpRequest):
        forget_pass = ForgetPassForm(request.POST)
        if forget_pass.is_valid():
            user_email = forget_pass.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user:
                send_email('تغییر کلمه عبور', user.email, {'user': user}, 'emails/reset-password.html')
                messages.success(request, 'لطفا ایمیل خود را چک کنید')
                return redirect(reverse('forget-pass-page'))

        context = {
            'forget_pass': forget_pass
        }
        return render(request, 'account_module/forget-pass.html', context)


class ResetPassView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login-page'))

        reset_pass = ResetPassForm()
        context = {
            'reset_pass': reset_pass
        }
        return render(request, 'account_module/reset-pass.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass = ResetPassForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass.is_valid():
            if user is None:
                return redirect(reverse('login-page'))
            else:
                new_user_pass = reset_pass.cleaned_data.get('password')
                user.set_password(new_user_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login-page'))

        context = {
            'reset_pass': reset_pass
        }
        return render(request, 'account_module/reset-pass.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
