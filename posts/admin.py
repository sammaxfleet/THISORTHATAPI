from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'updated_at')
    list_filter = ('owner', 'created_at')
    search_fields = ('title', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('owner')
        return queryset

admin.site.register(Post, PostAdmin)
