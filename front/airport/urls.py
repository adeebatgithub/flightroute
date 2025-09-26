from django.urls import path

from . import views
from . import views

urlpatterns = [
    path('', views.AirportListView.as_view(), name='airport-list'),
    path('add/', views.AirportCreateView.as_view(), name='airport-create'),
    path('edit/<int:pk>', views.AirportUpdateView.as_view(), name='airport-update'),
]
