from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason', 'email', 'created_at')
    search_fields = ('user__username', 'email', 'reason')
    list_filter = ('reason', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(ContactForm, ContactFormAdmin)
