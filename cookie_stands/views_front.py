from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand
from django.contrib.auth import get_user_model


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stand_detail.html"
    model = CookieStand
    context_object_name = "cookie_stand"


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stand_update.html"
    model = CookieStand
    fields = ["location", "description", "minimum_customers_per_hour",
              "maximum_customers_per_hour", "average_cookies_per_sale", "owner"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        return context


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stand_create.html"
    model = CookieStand
    fields = ["location", "description", "minimum_customers_per_hour",
              "maximum_customers_per_hour", "average_cookies_per_sale", "owner"]
    success_url = reverse_lazy('cookie_stand_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        return context


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_stand_list")
