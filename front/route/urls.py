from django.urls import path

from . import views
from . import views

urlpatterns = [
    path('', views.RouteListView.as_view(), name='route-list'),
    path('add/', views.RouteCreateView.as_view(), name='route-create'),
    path('edit/<int:pk>', views.RouteUpdateView.as_view(), name='route-update'),
]
