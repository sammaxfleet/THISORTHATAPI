from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'name')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('owner')
        return queryset

admin.site.register(Profile, ProfileAdmin)
