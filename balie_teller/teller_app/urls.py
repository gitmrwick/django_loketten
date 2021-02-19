from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('<int:pk>/', views.BalieView.as_view(), name='balie'),
        path('<int:pk>/trek', views.BalieView.as_view(), name='trek'),
        ]
