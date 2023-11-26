from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.forms import SearchForm
from product_module.models import Category, Product
from site_settings.models import FAQ, SiteSetting, FooterLinkBox


# Create your views here.


class Home(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['questions'] = FAQ.objects.filter(is_active=True).all()
        context['new_products'] = Product.objects.filter(is_active=True).order_by('-id')[:10]
        context['offer_products'] = Product.objects.filter(is_active=True, price2__isnull=False).order_by('-id')[:5]
        return context


def site_header_component(request):
    categories = Category.objects.filter(is_active=True)
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'categories': categories,
        'site_setting': site_setting,
    }
    return render(request, 'shared/site-header-components.html', context)


def site_footer_component(request):
    site_settings = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_box = FooterLinkBox.objects.all()
    context = {
        'site_setting': site_settings,
        'footer_link_box': footer_link_box
    }
    return render(request, 'shared/site-footer-components.html', context)
