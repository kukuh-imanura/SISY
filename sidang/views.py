from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelSidang, tabelWaktuSidang
from . forms import formSidang

def index(request) :

    if 'petugas_id' in request.session :

        tabel  = tabelSidang.objects.all()
        tabelWaktu  = tabelWaktuSidang.objects.all()
        dictionary = {
            'dataSidang'   : tabel,
            'dataWaktu'   : tabelWaktu,
        }
        return render(request, 'sidang/index.html', dictionary)
    
    elif 'mhs_id' in request.session : 

        mhs_id      = request.session['mhs_id']
        tabel       = tabelSidang.objects.filter(nim=mhs_id)
        dictionary = {
            'dataSidang'   : tabel,
        }
        return render(request, 'sidang/index.html', dictionary)
    
    else:
        return redirect('../')    

def tambah(request) :

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formSidang(request.POST, request.FILES)

        # VALIDASI FORM
        if form.is_valid():

            sidang = form.save(commit=False)

            # Set the foreign key values
            sidang.nim = form.cleaned_data['nim']
            # existing_sidang = sidang.objects.filter(nim=sidang.nim).exists()
            
            # if existing_sidang:
            #     # Data sidang sudah ada untuk nim tertentu
            #     messages.warning(request, 'Data sidang sudah ada untuk nim tersebut.')
            # else:
            #     sidang.save()
            #     return redirect('../')

            sidang.save()
            return redirect('../')
    
    else :
        form = formSidang()
        if 'mhs_id' in request.session:
            form.fields['nim'].initial = request.session['mhs_id']

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    return render(request, 'sidang/tambah.html', dictionary)

def update(request, id_sidang) :

    instance_sidang = get_object_or_404(tabelSidang, id_sidang=id_sidang)

    if request.method == 'POST':
        form = formSidang(request.POST, request.FILES, instance=instance_sidang)
        if form.is_valid():

            form.save()

            return redirect('../../')
    else:
        form = formSidang(instance=instance_sidang)
        form.fields['nim'].initial = instance_sidang.nim

    dictionary  = {
        'dataForm'      : form,
        'dataSidang'    : instance_sidang,
    }

    return render(request, 'sidang/update.html', dictionary)

def hapus(request, id_sidang):

    instance_sidang = get_object_or_404(tabelSidang, id_sidang=id_sidang)

    if instance_sidang.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'sidang/index.html', dictionary)


