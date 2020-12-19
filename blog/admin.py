from django.contrib import admin

# Register your models here.
from blog.models import Post,DukeLester,Category

admin.site.register(Post)

admin.site.register(DukeLester)

admin.site.register(Category)