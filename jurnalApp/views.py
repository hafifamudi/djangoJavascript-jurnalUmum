from django.shortcuts import render
from .models import Jurnal
from django.shortcuts import render,get_object_or_404
from .form import JurnalForm
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def daftar_jurnal(request):
    # mengambil object Jurnal dan membuat instance nya
    jurnals = Jurnal.objects.all()
    # mengirim data jurnals
    return render(request, 'mainJurnal.html',{'jurnals':jurnals})

def simpan_jurnal(request, form, template_name):
    # variable untuk menampung data dalam bentuk dictionary
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # mengirim variable data dengan index form_is_valid
            data['form_is_valid'] = True
            jurnals = Jurnal.objects.all()
            data['html_daftar_jurnal'] = render_to_string('list_jurnal.html',{
                'jurnals':jurnals
            })
            
        else:
            data['form_is_valid'] = False
    context = {'form':form}
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def buatJurnal(request):
    if request.method == 'POST':
        # mengirim form dengan request POST
        form = JurnalForm(request.POST)
    else:
        # mengirim form tanpa request
        form = JurnalForm()
    return simpan_jurnal(request,form,"createJurnal.html")

def ubahJurnal(request,pk):
    # mengambil object jurnal dengan ID
    jurnal = get_object_or_404(Jurnal,pk=pk)
    if request.method == 'POST':
        # mengirim form dengan request POST dan ID
        form = JurnalForm(request.POST,instance=jurnal)
    else:
        # mengirim form dengan request POST tanpa ID 
        form = JurnalForm(instance=jurnal)
    return simpan_jurnal(request,form,"updateJurnal.html")

def hapusJurnal(request,pk):
    data = dict()
    # mengambil object jurnal dengan ID
    jurnal = get_object_or_404(Jurnal,pk=pk)
    if request.method == 'POST':
        jurnal.delete()
        # mengirim variable data dengan index form_is_valid
        data['form_is_valid'] = True
        jurnals = Jurnal.objects.all()
        data['html_daftar_jurnal'] = render_to_string("list_jurnal.html",{
            'jurnals':jurnals
        })  
    else:
        context = {'jurnal':jurnal}
        data['html_form'] = render_to_string("deleteJurnal.html",
            context,
            request=request,
        )
    return JsonResponse(data)

