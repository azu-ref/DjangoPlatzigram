#django
from django.contrib import admin
#from django.contrib.auth.models import User

#models
from posts.models import Post
# from users.models import Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ('profile', 'title', 'photo', 'created')
    
    list_display_links =  ('title',)
    
    search_fields = (
        'user__email',
        'user__username', 
        'profile__phone_number',
        'title'
        )

    list_filter = (
        'created',
        'modified',
    )

