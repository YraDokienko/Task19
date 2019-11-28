from .forms import PizzaForm, PizzaPriceUpdateForm, PizzaSortedForm
from django.views.generic import ListView, FormView, UpdateView
from django.shortcuts import render
from .models import Pizza



class PizzaHomeView(ListView):
    model = Pizza
    template_name = 'pizza_home.html'


    def get_queryset(self):
        sort = self.request.GET.get('sort_order', 'name')
        return Pizza.objects.all().order_by(sort)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Pizza.objects.all().count()
        context['list'] = Pizza.objects.values_list('name', flat=True)
        context['form'] = PizzaSortedForm
        return context


class PizzaFormAddView(FormView):
    template_name = 'form_pizza_add.html'
    form_class = PizzaForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PizzaUpdateView(UpdateView):
    form_class = PizzaForm
    model = Pizza
    template_name = 'form_pizza_add.html'
    success_url = '/'


class PizzaPriceUpdateView(FormView):
    template_name = 'pizza_price_update.html'
    form_class = PizzaPriceUpdateForm
    success_url = '/'

    def form_valid(self, form):
        value = form.cleaned_data
        pizzas = Pizza.objects.all()
        for pizza in pizzas:
            pizza.price = pizza.price + value['value']
            pizza.save()
        return super().form_valid(form)
