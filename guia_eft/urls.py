
from django.contrib import admin
from django.urls import path
from app_tarkov.views import vista_index, vista_Mapas, vista_Bosses, vista_Ammo, vista_api, vista_Armor, vista_formulario, vista_login
from app_tarkov.views import RegistroListView, RegistroCreateView, RegistroUpdateView, RegistroDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_index, name='index'),
    path('Bosses/', vista_Bosses, name='Bosses'),
    path('Ammo/', vista_Ammo, name='Ammo'),
    path('api/', vista_api, name='api'),
    path('Armor/', vista_Armor, name='Armor'),
    path('formulario/', vista_formulario, name='formulario'),
    path('login/', vista_login, name='login'),
    path('Mapas/', vista_Mapas, name='Mapas'),
    path('registros/', RegistroListView.as_view(), name='registro_list'),
    path('registros/crear/', RegistroCreateView.as_view(), name='registro_create'),
    path('registros/<int:pk>/', RegistroUpdateView.as_view(), name='registro_edit'),
    path('registros/<int:pk>/eliminar/', RegistroDeleteView.as_view(), name='registro_delete'),
    path('registros/<int:pk>/editar/', RegistroUpdateView.as_view(), name='registro_edit'),

]









