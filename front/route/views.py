from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from front.models import RouteModel
from .forms import RouteForm


class RouteListView(generic.ListView):
    model = RouteModel
    template_name = "route/list.html"
    context_object_name = "routes"


class RouteCreateView(SuccessMessageMixin, generic.CreateView):
    model = RouteModel
    form_class = RouteForm
    template_name = "route/create.html"
    success_message = "Route Created"
    success_url = reverse_lazy("route-list")


class RouteUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = RouteModel
    form_class = RouteForm
    template_name = "route/update.html"
    success_message = "Route Updated"
    success_url = reverse_lazy("route-list")
