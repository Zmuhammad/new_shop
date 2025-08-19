from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm , UserCreateForm
from .models import User , OtpCode
from django.contrib.auth.models import Group


# Register your models here.

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number' , 'code' , 'created')  


class UserAdmin (BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email' , 'phone_number' , 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login' , )

    fieldsets = (
        ('main info' , {'fields': ('email' , 'phone_number' , 'full_name' , 'password')}),
        ('permissions' ,{'fields': ('is_active' , 'is_admin' , 'last_login' , 'is_superuser' , 'groups' , 'user_permissions' )}),
    )
    
    add_fieldsets = (
        (None , {'fields': ('phone_number' , 'email' , 'full_name' , 'password1' , 'password2' )}),

    )

    search_fields = ('email' , 'full_name')
    ordering = ('full_name',)

    filter_horizontal = ('groups' , 'user_permissions')

    # def get_form(self, request, obj = None, **kwargs):
    #     form =  super().get_form(request, obj, **kwargs) 
    #     is_superuser = request.user.is_superuser
    #     if not is_superuser :
    #         form.base_fields['is_superuser'].disabled = True
    #     return form


admin.site.register(User , UserAdmin)

# admin.site.unregister(Group)

