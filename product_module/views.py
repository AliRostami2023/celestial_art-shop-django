from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from product_module.forms import SearchForm
from product_module.models import Product, ProductImage


# Create your views here.

class ProductList(ListView):
    template_name = 'product_module/product-list.html'
    model = Product
    paginate_by = 16
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        query = super().get_queryset()
        form = SearchForm(self.request.GET)

        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            query = query.filter(Q(title__icontains=search_query))

        category_name = self.kwargs.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetail(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        lated_product = self.object
        context['product_image'] = ProductImage.objects.filter(product_id=lated_product.id).all()
        return context
