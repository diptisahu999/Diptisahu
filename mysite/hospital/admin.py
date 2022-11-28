from django.contrib import admin
from hospital.models import Hospital,Docter

# Register your models here.
@admin.register(Hospital)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','f_name','l_name','email','mobile','password']


@admin.register(Docter)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','f_name','l_name','email','password','mobile','specilist','pic']

