from django.contrib import admin
from .models import Follower

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'followed__username')
    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('owner', 'followed')
        return queryset

admin.site.register(Follower, FollowerAdmin)
