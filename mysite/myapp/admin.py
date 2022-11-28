from django.contrib import admin
from .models import User, Appo
# Register your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display =['id','f_name','l_name','email','password','mobile','gender','description']

# admin.site.register(Appo)
@admin.register(Appo)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','name','email','date','amount','time']
