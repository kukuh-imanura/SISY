from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelYudisium
from . forms import formYudisium, formTglYudisium

def index(request) :

    if 'petugas_id' in request.session :
        tabel  = tabelYudisium.objects.all()
        dictionary = {
            'dataYudisium'   : tabel
        }
        return render(request, 'yudisium/index.html', dictionary)
    
    elif 'mhs_id' in request.session : 

        mhs_id = request.session['mhs_id']
        tabel = tabelYudisium.objects.filter(nim=mhs_id)
        dictionary = {
            'dataYudisium'   : tabel
        }
        return render(request, 'yudisium/index.html', dictionary)
    
    else:
        return redirect('../')

def tambah(request) :

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formYudisium(request.POST, request.FILES)
        formTgl = formTglYudisium(request.POST)

        if 'petugas_id' in request.session :
        # VALIDASI FORM
            if form.is_valid() and formTgl.is_valid() :

                
                tgl = formTgl.cleaned_data['tanggal']

                yudisium = form.save(commit=False)

                # Set the foreign key values
                yudisium.nim = form.cleaned_data['nim']

                yudisium.tanggal = tgl
                yudisium.tanggal = "0001-01-01 00:00:00.000000"

                yudisium.save()

                return redirect('../')
            
        elif 'mhs_id' in request.session :
            if form.is_valid() :

                yudisium = form.save(commit=False)

                # Set the foreign key values
                yudisium.nim = form.cleaned_data['nim']
                yudisium.tanggal = "0001-01-01 00:00:00.000000"

                yudisium.save()

                return redirect('../')
        
    else :
        form = formYudisium()
        formTgl = formTglYudisium()
        if 'mhs_id' in request.session:
            form.fields['nim'].initial = request.session['mhs_id']

    # DICTIONARY
    dictionary = {
        'dataForm'  : form,
        'dataFormTgl'  : formTgl,
    }

    return render(request, 'yudisium/tambah.html', dictionary)

def update(request, id_yudisium) :

    instance_yudisium = get_object_or_404(tabelYudisium, id_yudisium=id_yudisium)

    if request.method == 'POST':
        form = formYudisium(request.POST, request.FILES, instance=instance_yudisium)
        formTgl = formTglYudisium(request.POST, instance=instance_yudisium)

        if 'petugas_id' in request.session :

            if form.is_valid() and formTgl.is_valid() :

                tgl = formTgl.cleaned_data['tanggal']

                yudisium = form.save(commit=False)
                yudisium.tanggal = tgl

                yudisium.save()

                return redirect('../../')
            
        elif 'mhs_id' in request.session : 
            if form.is_valid() :

                yudisium = form.save(commit=False)
                yudisium.tanggal = "0001-01-01 00:00:00.000000"
                yudisium.save()

                return redirect('../../')
    else:
        form = formYudisium(instance=instance_yudisium)
        formTgl = formTglYudisium(instance=instance_yudisium)
        form.fields['nim'].initial = instance_yudisium.nim

    dictionary  = {
        'dataForm'      : form,
        'dataFormTgl'      : formTgl,
        'dataYudisium'    : instance_yudisium,
    }

    return render(request, 'yudisium/update.html', dictionary)

def hapus(request, id_yudisium):

    instance_yudisium = get_object_or_404(tabelYudisium, id_yudisium=id_yudisium)

    if instance_yudisium.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'yudisium/index.html', dictionary)


