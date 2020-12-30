from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from accounts.models import Profile


class AccountAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number','first_name', 'last_name', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_number','visit_counter')
    def first_name(self,obj):
        return obj.account.first_name
    def last_name(self,obj):
        return obj.account.last_name
    def phone_number(self,obj):
        return obj.account.phone_number
admin.site.register(get_user_model(), AccountAdmin)
admin.site.register(Profile, ProfileAdmin)