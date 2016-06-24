from django.contrib import admin

# Register your models here.

from the_blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):

    list_display = ["__str__", "created", "updated"]
    list_filter = ["created", "updated"]
    search_fields = ["title", "content"]

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)
