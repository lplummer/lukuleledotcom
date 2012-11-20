from django.contrib import admin
from models import *

from django.contrib.auth.models import User

class BlogPostAdmin(admin.ModelAdmin):
	pass
admin.site.register(BlogPost, BlogPostAdmin)

# formfield_overrides = {
    # models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
# }