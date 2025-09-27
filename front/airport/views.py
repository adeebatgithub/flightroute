# Django imports for views and success messaging
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

# Local imports
from front.models import AirportModel
from .forms import AirportForm


class AirportListView(generic.ListView):
    """Display all airports in a list"""
    model = AirportModel
    template_name = "airport/list.html"
    context_object_name = "airports"


class AirportCreateView(SuccessMessageMixin, generic.CreateView):
    """Create new airport with success message"""
    model = AirportModel
    form_class = AirportForm
    template_name = "airport/create.html"
    success_message = "Airport Created"
    success_url = reverse_lazy("airport-list")  # Redirect to list after creation


class AirportUpdateView(SuccessMessageMixin, generic.UpdateView):
    """Update existing airport with success message"""
    model = AirportModel
    form_class = AirportForm
    template_name = "airport/update.html"
    success_message = "Airport Updated"
    success_url = reverse_lazy("airport-list")  # Redirect to list after update