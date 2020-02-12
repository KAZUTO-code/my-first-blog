from django.contrib import admin
from blog.models import Post, Comment

#admin.site.register(Post)
#admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'text', 'created_date', 'published_date',)
    list_display_links = ('author', 'title')


admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
