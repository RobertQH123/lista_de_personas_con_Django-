from django.urls import path
from .views import (
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView
    )
app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name = 'persona-details'),
    path('create/', PersonaCreateView.as_view(), name = 'persona-create'),
    ]