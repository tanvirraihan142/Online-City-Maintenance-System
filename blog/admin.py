from django.contrib import admin
from blog.models import Post, Comment, Catogery, Status


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Catogery)
admin.site.register(Status)
