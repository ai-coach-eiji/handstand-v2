from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='pose_estimation/index.html'), name='index'),
    path('upload/', views.upload, name='upload'),
    path('tos/', views.terms_of_service, name='tos'),
]