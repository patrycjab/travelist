from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import CustomUser, SourcePoints, Transaction


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff',
                    'balance', 'referrer_email')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('balance', 'referrer_email')
        }),
    )


@admin.register(SourcePoints)
class SourcePointsAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
