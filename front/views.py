from django.views import generic

from .forms import FindNthNodeForm, ShortPathForm
from .utils import find_longest_path_from_airport, find_nth_node, find_shortest_path


class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        longest_path = find_longest_path_from_airport()
        context.update({
            "longest_path": longest_path["path"],
            "longest_path_duration": longest_path["duration"],
            "form_nth": FindNthNodeForm,
            "form_short_path": ShortPathForm,
        })
        return context


class NthNodeFormView(generic.FormView, DashboardView):
    form_class = FindNthNodeForm
    template_name = "dashboard.html"

    def form_valid(self, form):
        starting = form.cleaned_data.get('starting')
        direction = form.cleaned_data.get('direction')
        n = form.cleaned_data.get('n')

        context = super().get_context_data()
        context.update({
            "nth_node": find_nth_node(starting, direction, n),
        })
        return self.render_to_response(context)


class ShortestPathFormView(generic.FormView, DashboardView):
    form_class = ShortPathForm
    template_name = "dashboard.html"

    def form_valid(self, form):
        starting = form.cleaned_data.get('starting')
        end = form.cleaned_data.get('end')

        context = super().get_context_data()
        shortest_path = find_shortest_path(starting, end)
        context.update({
            "short_path": shortest_path["path"],
            "short_path_duration": shortest_path["duration"],
        })
        return self.render_to_response(context)
