from django.contrib import admin
from .models import UpdatedUser
from django.contrib.auth.admin import UserAdmin

# URL: https://www.youtube.com/watch?v=8jyyuBaZwVU
# This tutorial taught me how to inherit and use AbstractUser


class UpdatedUserAdmin(UserAdmin):
    """ Custom Admin control for UpdatedUsers """
    model = UpdatedUser
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Seller Status', {'fields': ('seller_status',)}),
    )
    list_display = (
        'id',
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'seller_status',
    )
    ordering = ('username',)


admin.site.register(UpdatedUser, UpdatedUserAdmin)
