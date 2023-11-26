from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView

from account_module.models import User
from dashboard_user.forms import ChangePasswordUserForm
from order_module.models import Order, OrderDetail
from site_settings.models import SiteSetting


# Create your views here.

@method_decorator(login_required, name='dispatch')
class DashboardUser(TemplateView):
    template_name = 'dashboard_user/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = User.objects.filter(id=self.request.user.id).first()
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context


def menu_dashboard(request):
    return render(request, 'dashboard_user/components/menu-dashboard.html')


@method_decorator(login_required, name='dispatch')
class ChangePasswordUser(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordUserForm()
        return render(request, 'dashboard_user/change-password-user.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ChangePasswordUserForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('current_password', 'کلمه عبور فعلی صحیح نیست')

        return render(request, 'dashboard_user/change-password-user.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyShopping(ListView):
    model = Order
    template_name = 'dashboard_user/shopping-user.html'
    context_object_name = 'order'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id, is_paid=True)
        return queryset


@login_required
def my_shopping_detail(request: HttpRequest, order_id):
    order = Order.objects.prefetch_related('orderdetail_set').filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('سبد خرید مورد نظر یافت نشد')

    return render(request, 'dashboard_user/shopping-detail-user.html', {
        'order': order
    })
