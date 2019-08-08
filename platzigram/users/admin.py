#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    #En esta variable indicamos que campos queremos ver en la tabla de perfiles que django 
    #crea para administrarlos, tenemos que tener nuestro modelo previamente registrado
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture') 
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name', 
        'phone_number'
        )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
        )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                )
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    #Profile in-line for users

    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    # Define a new User admin
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
