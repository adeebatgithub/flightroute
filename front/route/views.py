# Django imports for views and success messaging
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

# Local imports
from front.models import RouteModel
from .forms import RouteForm


class RouteListView(generic.ListView):
    """Display all routes in a list"""
    model = RouteModel
    template_name = "route/list.html"
    context_object_name = "routes"


class RouteCreateView(SuccessMessageMixin, generic.CreateView):
    """Create new route with success message"""
    model = RouteModel
    form_class = RouteForm
    template_name = "route/create.html"
    success_message = "Route Created"
    success_url = reverse_lazy("route-list")  # Redirect to list after creation


class RouteUpdateView(SuccessMessageMixin, generic.UpdateView):
    """Update existing route with success message"""
    model = RouteModel
    form_class = RouteForm
    template_name = "route/update.html"
    success_message = "Route Updated"
    success_url = reverse_lazy("route-list")  # Redirect to list after update
