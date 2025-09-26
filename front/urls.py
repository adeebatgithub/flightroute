from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('nth-node/', views.NthNodeFormView.as_view(), name='nth-node'),
    path('short-path/', views.ShortestPathFormView.as_view(), name='short-path'),

    path('airport/', include("front.airport.urls")),
    path('route/', include("front.route.urls")),
]
