from django.contrib import admin
from .models import *


# Register your models here.

class contextAdmin(admin.ModelAdmin):
    list_display = ('id', 'titleOrg', 'category', 'pubDate')


class tokensAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'posting')


class idfAdmin(admin.ModelAdmin):
    list_display = ('token', 'idf')

#
# class categoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'docList')


class tfIdfListAdmin(admin.ModelAdmin):
    list_display = ('doc', 'tfIdfFirstList', 'tfIdfSecondList', 'lengthFirst', 'lengthSecond')


admin.site.register(DataScraped, contextAdmin)
admin.site.register(Tokens, tokensAdmin)
admin.site.register(Idf, idfAdmin)
admin.site.register(TfIdfList, tfIdfListAdmin)
# admin.site.register(Category, categoryAdmin)
