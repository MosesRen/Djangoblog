from django.contrib import admin
from index.models import *
# Register your models here.
class  Catagoryadmin(admin.ModelAdmin):
    list_display = ['name']
class  Tagadmin(admin.ModelAdmin):
    list_display = ['name']
class blogpost(admin.ModelAdmin):
    def show_all_tags(self, obj):
        return [a.name for a in obj.tags.all()]
    list_display = ['title','catagory','show_all_tags','text','time']
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','text','img']
admin.site.register(ArticleTag, Tagadmin)
admin.site.register(ArticleCatagory, Catagoryadmin)
admin.site.register(blogtext,blogpost)
admin.site.register(aboutme,AboutAdmin)

# admin.site.register([ArticleCatagory,ArticleTag,blogtext,aboutme])