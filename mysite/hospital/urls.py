from django.urls import path,include
from . import views

urlpatterns = [
    path('hospital/',views.hospitalindex,name='hospitalindex'),
    path('hospitallogin/',views.hospitallogin,name='hospitallogin'),
    path('logout',views.logout,name='logout'),
    path('docter',views.docter,name='docter'),
    path('register/',views.register,name='register'),
    path('delete/<int:pid>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('patient/',views.patient,name='patient'),
    path('delet/<int:id>',views.delet,name='delet'),
]