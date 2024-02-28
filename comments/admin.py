from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'post', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'post__title', 'content')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('owner', 'post')
        return queryset

admin.site.register(Comment, CommentAdmin)
