from django.contrib import admin
from .models import  Category,Page, UserProfile


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['title','category','url']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','views','likes']

# Add in this class to customized the Admin Interface
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)