from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^perfil$', views.usuario, name='perfil'),
    url(r'^buscar$', views.buscar, name='buscar'),
    url(r'^insertar$', views.insertar, name='insertar'),
    url(r'^insertado$', views.insertado, name='insertado'),
    url(r'^modificar$', views.modificar, name='modificar'),
    url(r'^modificado$', views.modificado, name='modificado'),
    url(r'^mostrar$', views.mostrar, name='mostrar'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^registrado$', views.registrado, name='registrado'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^guarda_plato$', views.guardarPlato, name='guarda_plato'),
    url(r'^listar_platos$', views.listarplatos, name='listar_platos'),
    url (r'^mostrarajax$',views.mostrarajax, name = 'mostrarajax'),
    url (r'^lazy_load_posts$',views.lazy_load_posts, name = 'lazy_load_posts'), 

]
