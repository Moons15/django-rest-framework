from django.contrib import admin

from rest_framework.authtoken.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user','business','contact', 'created')
    fields = ('user','business','contact')
    ordering = ('-created',)


admin.site.register(Token, TokenAdmin)
