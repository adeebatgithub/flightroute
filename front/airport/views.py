from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from front.models import AirportModel
from .forms import AirportForm


class AirportListView(generic.ListView):
    model = AirportModel
    template_name = "airport/list.html"
    context_object_name = "airports"


class AirportCreateView(SuccessMessageMixin, generic.CreateView):
    model = AirportModel
    form_class = AirportForm
    template_name = "airport/create.html"
    success_message = "Airport Created"
    success_url = reverse_lazy("airport-list")


class AirportUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = AirportModel
    form_class = AirportForm
    template_name = "airport/update.html"
    success_message = "Airport Updated"
    success_url = reverse_lazy("airport-list")
