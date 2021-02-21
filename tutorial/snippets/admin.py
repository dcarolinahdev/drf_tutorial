"""User admin classes."""

# Django
from django.contrib import admin

# Models
from snippets.models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
	"""Snippet admin."""

	list_display = ('title', 'linenos', 'language', 'style')

	search_fields = (
		'title',
		'language'
	)

	readonly_fields = ('created',)
