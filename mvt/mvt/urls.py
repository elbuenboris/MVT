from django.contrib import admin
from django.urls import path
from mvt.views import saludo, segundo_template, template_con_lista
from family.views import create_member, members_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name = 'saludo'),
    path('segundo_template/', segundo_template, name='segundo_template'),
    path('template_con_lista/', template_con_lista, name='template_con_lista'),
    path('create_member/', create_member, name = 'create_member'),
    path('members_list/', members_list, name = 'members_list' )
]
