from django.conf.urls import patterns,url
from .views import IndexView,NuevoUsuario
 

urlpatterns = patterns('',     

    url(r'^$', IndexView.as_view(),name='home'),
    url(r'^salir/$','principal.views.LogOut'),
    url(r'^nuevousuario/$',NuevoUsuario.as_view(),name='nuevousuario'),
     
)
