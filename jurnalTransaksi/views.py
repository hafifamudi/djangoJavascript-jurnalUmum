from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from .models import transaksiJurnal
from jurnalApp.models import Jurnal 
from .forms import jurnalTransaksiForm
from django.urls import reverse_lazy

class daftarJurnalTransaksi(View):
    template_name = 'daftar_jurnal.html'
    # menggunakan fungsi get di dalam View untuk melakukan GET reqeust
    def get(self,request,idJurnal):
        jurnal = Jurnal.objects.get(pk=idJurnal)
        daftar_jurnal = transaksiJurnal.objects.filter(jurnal=jurnal)

        daftar_hasil = [] #variable dengan tipe list untuk menampung data lebih dari satu
        total_debt   = [] #variable untuk menampung hasil debit menggunakan list , karna lebih dari satu
        total_kredit = [] #variable untuk menampung hasil kredit menggunakan list,karnam lebih dari satu
        kas = 0 #variable untuk menampung kas
        hasil_debt   = 0
        hasil_kredit = 0
        for trans in daftar_jurnal:
            kas = kas + (trans.debt - trans.kredit)
            #variable hasil(dict) untuk menampung properti data object Jurnal
            hasil = {
            'id': trans.pk,
            'tanggalJurnal':trans.tanggalJurnal,
            'uraianJurnal':trans.uraianJurnal,
            'debt':trans.debt,
            'kredit':trans.kredit,
            'kas':kas
            }
            # hasil debit dan kredit yang di tampung pada list deb dan kredit akan di tambah dengan method sum
            # sebelum di tambahkan, terlebih dahulu kita mengcasting / merubah tipe data float menjadi int agar hasil memberikan nilai non decimal
            debt = int(float(trans.debt))
            kredit = int(float(trans.kredit))
            #menambahkan variable hasil,debt, dan kredit pada variable daftar_hasil,hasil_debt dan hasil_kredit
            total_debt.append(debt)
            total_kredit.append(kredit)
            # menampung hasil dari penambahan debit dan kredit pada variable hasil_debt dan hasil_kredit
            hasil_debt   =  sum(total_debt)
            hasil_kredit =  sum(total_kredit)
            daftar_hasil.append(hasil)
        form = jurnalTransaksiForm(request.POST)
        #menampung semua data pada variable data(dict) untuk di kirim kan Ke template_name
        data = {
            'jurnal':jurnal,
            'daftar_hasil':daftar_hasil,
            'total_kas':kas,
            'total_debt':hasil_debt,
            'total_kredit':hasil_kredit,
        }
        return render(request,self.template_name,data)

class tambahJurnalTransaksi(View):
    template_name = 'createJurnalTransaksi.html'
    # menggunakan fungsi get di dalam View untuk melakukan GET reqeust
    def get(self,request,idJurnal):
        form = jurnalTransaksiForm(request.POST)
        # mengirim data menggunakan dict yang terdiri dari instance form dan idJurnal
        data = {
            'form':form,
            'idJurnal':idJurnal
        }
        return render(request,self.template_name,data)

class simpanJurnalTransaksi(View):
    #menggunakan fungsi post untuk memposting data
    def post(self,request,idJurnal):
            form = jurnalTransaksiForm(request.POST)
            if form.is_valid():
                #mengambil data Jurnal Dengan ID 
                jurnal = Jurnal.objects.get(pk=idJurnal)
                #membuat instance dari pada object jurnalTransaksiForm dengan nama variable transaksiJurnal
                jurnalTransaksi = transaksiJurnal()
                jurnalTransaksi.jurnal = jurnal
                #ambil data dari form
                jurnalTransaksi.tanggalJurnal = form.cleaned_data['tanggalJurnal']
                jurnalTransaksi.uraianJurnal  = form.cleaned_data['uraianJurnal']
                jurnalTransaksi.debt          = form.cleaned_data['debt']
                jurnalTransaksi.kredit        = form.cleaned_data['kredit']
                #simpan data yang telah di kirim melalui form
                jurnalTransaksi.save()
                #mengirimakan argumen dalam bentuk dict menggunakan kwargs
                return redirect(reverse_lazy('jurnalTransaksi:indexTransaksi',kwargs={
                    'idJurnal':idJurnal
                }))

class ubahJurnalTransaksi(View):
    template_name = 'updateJurnalTransaksi.html'
    def get(self,request,idJurnal,idLama):
        # mengambil data object jurnal dengan Id bersangkutan
        jurnal = Jurnal.objects.get(pk=idJurnal)
        jurnalTransaksi = transaksiJurnal.objects.get(jurnal=jurnal,pk=idLama)
        # mengambil data yang telah di filter dari instance jurnal
        daftar_jurnalTransaksi = transaksiJurnal.objects.filter(jurnal=jurnal)
        # variable untuk tampung data
        # mengambil data lama
        data_lama = {
            'id':jurnalTransaksi.pk,
            'tanggalJurnal':jurnalTransaksi.tanggalJurnal,
            'uraianJurnal':jurnalTransaksi.uraianJurnal,
            'debt':jurnalTransaksi.debt,
            'kredit':jurnalTransaksi.kredit
        }
        # mengisi data lama dengan keyword initial dengan variable data_lama
        form = jurnalTransaksiForm(initial=data_lama)
        data_ubah = {
            'jurnal':jurnal,
            'form':form,
            'jurnalTransaksi':jurnalTransaksi
        }

        return render(request,self.template_name,data_ubah)

class updateJurnalTransaksi(View):
    def post(self,request,idJurnal):
        form = jurnalTransaksiForm(request.POST)
        if form.is_valid():
            jurnal = Jurnal.objects.get(pk=idJurnal)
            # ambil data form id 
            jurnalTransaksiID = form.cleaned_data['id']
            # masukan data form id untuk pengambilan data jurnal Transaksi
            jurnalTransaksi = transaksiJurnal.objects.get(pk=jurnalTransaksiID)
            # memasukan data jurnal Transaksi ke dalam model jurnal Transaksi 
            jurnalTransaksi.jurnal = jurnal
            # ambil data dari setiap field form
            jurnalTransaksi.tanngalJurnal = form.cleaned_data['tanggalJurnal']
            jurnalTransaksi.uraianJurnal  = form.cleaned_data['uraianJurnal']
            jurnalTransaksi.debt   = form.cleaned_data['debt']
            jurnalTransaksi.kredit = form.cleaned_data['kredit']
            jurnalTransaksi.save()
            #mengirimkan data id melalui kwargs
            return redirect(reverse_lazy('jurnalTransaksi:indexTransaksi',kwargs={
                    'idJurnal':idJurnal
                }))

class hapusJurnalTransaksi(View):
    def get(self,request,idJurnal,idLama):
        jurnal = Jurnal.objects.get(pk=idJurnal)
        jurnalTransaksi = transaksiJurnal.objects.get(jurnal=jurnal,pk=idLama)

        # mengambil data dari instance transaksiJurnal lalu jika True maka hapus data
        if jurnalTransaksi:
            jurnalTransaksi.delete()

            return redirect(reverse_lazy('jurnalTransaksi:indexTransaksi',kwargs={
                'idJurnal':idJurnal
            }))        
        