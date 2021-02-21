"""Urls models."""

# Django
from django.urls import path

# Additional apps
from snippets import views

urlpatterns = [
	path('snippets/', views.snippet_list),
	path('snippets/<int:pk>/', views.snippet_detail),
]
