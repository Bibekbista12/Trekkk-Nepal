from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrekListView.as_view(), name='trek-list'),
    path('trek/<slug:slug>/', views.TrekDetailView.as_view(), name='trek-detail'),
]