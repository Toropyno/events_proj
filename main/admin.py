from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class UserChangeForm(forms.ModelForm):
    """
    Форма для изменения данных пользователя
    """
    password = ReadOnlyPasswordHashField(help_text='<a href="../password/">Сменить пароль</a>')

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm

    list_display = (
        'email',
        'id',
    )
    list_filter = (

    )
    ordering = (

    )
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password'
            )
        }),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
    )
