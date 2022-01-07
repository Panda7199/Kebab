from django.contrib import admin
from home.models import Aboutus, Chef, ContactMessage, Order, Comment_cheff

class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title','email', 'phone',]

class ChefAdmin(admin.ModelAdmin):
    list_display = ['title','image', 'description',]



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'creat_at',)
    list_filter = ['status']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'amount', 'category', 'food', 'address','ip',]
    list_filter = ['status']

class Comment_cheffAdmin(admin.ModelAdmin):
    list_display = ['name',  'email', 'comment',]
    list_filter = ['status']
    readonly_fields = ('name', 'email', 'comment', 'ip',)



admin.site.register(Comment_cheff, Comment_cheffAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Aboutus, AboutusAdmin)