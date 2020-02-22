from django.urls import path
from . import views

urlpatterns = [
    path('<int:idJurnal>',views.daftarJurnalTransaksi.as_view(),name='indexTransaksi'),    
    path('<int:idJurnal>/buatJurnalTransksi/',views.tambahJurnalTransaksi.as_view(),name='simpanTransaksiPage'),
    path('<int:idJurnal>/simpanJurnalTransksi/',views.simpanJurnalTransaksi.as_view(),name='simpanTransaksi'),
    path('<int:idJurnal>/<int:idLama>/ubahJurnalTransaksi/',views.ubahJurnalTransaksi.as_view(),name='ubahJurnal'),
    path('<int:idJurnal>/simpanPerubahanJurnal/',views.updateJurnalTransaksi.as_view(),name='updateJurnal'),
    path('<int:idJurnal>/<int:idLama>/hapusJurnalTransaksi/',views.hapusJurnalTransaksi.as_view(),name='hapusJurnal')
]