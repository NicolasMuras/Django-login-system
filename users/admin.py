from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Quota


class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'is_admin', 'is_active', 'date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email','password')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

class QuotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'max_resources')


admin.site.register(User, UserAdmin)
admin.site.register(Quota, QuotaAdmin)
