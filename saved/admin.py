from django.contrib import admin
from .models import Saved

class SavedAdmin(admin.ModelAdmin):
    list_display = ('owner', 'post', 'created_at')
    list_filter = ('owner', 'created_at')
    search_fields = ('owner__username', 'post__title')
    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('owner', 'post')
        return queryset

admin.site.register(Saved, SavedAdmin)
