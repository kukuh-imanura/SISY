from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelSidang
from . forms import formSidang, formTglSidang

def index(request) :

    if 'petugas_id' in request.session :

        tabel  = tabelSidang.objects.all()
        dictionary = {
            'dataSidang'   : tabel,
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
        formTgl = formTglSidang(request.POST)

        if 'petugas_id' in request.session :

            # VALIDASI FORM
            if form.is_valid() and formTgl.is_valid() :

                
                tgl = formTgl.cleaned_data['tanggal']

                sidang = form.save(commit=False)

                # Set the foreign key values
                sidang.nim = form.cleaned_data['nim']
                sidang.tanggal = tgl

                sidang.save()
                return redirect('../')
            
        elif 'mhs_id' in request.session :

            # VALIDASI FORM
            if form.is_valid() :

                sidang = form.save(commit=False)

                # Set the foreign key values
                sidang.nim = form.cleaned_data['nim']
                sidang.tanggal = "0001-01-01 00:00:00.000000"

                sidang.save()
                return redirect('../')
    
    else :
        form = formSidang()
        formTgl = formTglSidang()
        if 'mhs_id' in request.session:
            form.fields['nim'].initial = request.session['mhs_id']

    # DICTIONARY
    dictionary = {
        'dataForm'  : form,
        'dataFormTgl'  : formTgl,
    }

    return render(request, 'sidang/tambah.html', dictionary)

def update(request, id_sidang) :

    instance_sidang = get_object_or_404(tabelSidang, id_sidang=id_sidang)

    if request.method == 'POST':
        form = formSidang(request.POST, request.FILES, instance=instance_sidang)
        formTgl = formTglSidang(request.POST, instance=instance_sidang)

        if 'petugas_id' in request.session :
            if form.is_valid() or formTgl.is_valid() :

                
                tgl = formTgl.cleaned_data['tanggal']

                sidang = form.save(commit=False)

                sidang.tanggal = tgl
                sidang.tanggal = "0001-01-01 00:00:00.000000"

                sidang.save()

                return redirect('../../')
        
        if 'mhs_id' in request.session :
            if form.is_valid() :

                sidang = form.save(commit=False)

                sidang.tanggal = "0001-01-01 00:00:00.000000"

                sidang.save()

                return redirect('../../')
            
    else:
        form = formSidang(instance=instance_sidang)
        formTgl = formTglSidang()
        form.fields['nim'].initial = instance_sidang.nim

    dictionary  = {
        'dataForm'      : form,
        'dataFormTgl'   : formTgl,
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


