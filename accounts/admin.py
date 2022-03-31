from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
<<<<<<< HEAD
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.
=======
from .models import Account,UserProfile
from django.utils.html import format_html

>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
<<<<<<< HEAD

=======
    
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

<<<<<<< HEAD
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
=======
admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
