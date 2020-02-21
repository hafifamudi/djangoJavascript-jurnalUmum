from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<idJurnal>\d+)$',views.daftarJurnalTransaksi.as_view(),name='indexTransaksi'),    
    url(r'(?P<idJurnal>\d+)/buatJurnalTransksi/$',views.tambahJurnalTransaksi.as_view(),name='simpanTransaksiPage'),
    url(r'(?P<idJurnal>\d+)/simpanJurnalTransksi/$',views.simpanJurnalTransaksi.as_view(),name='simpanTransaksi'),
    url(r'(?P<idJurnal>\d+)/(?P<idLama>\d+)/ubahJurnalTransaksi/$',views.ubahJurnalTransaksi.as_view(),name='ubahJurnal'),
    url(r'(?P<idJurnal>\d+)/simpanPerubahanJurnal/$',views.updateJurnalTransaksi.as_view(),name='updateJurnal'),
    url(r'(?P<idJurnal>\d+)/(?P<idLama>\d+)/hapusJurnalTransaksi/$',views.hapusJurnalTransaksi.as_view(),name='hapusJurnal')
]