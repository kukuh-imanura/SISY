import hashlib
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelSidang
from . forms import formSidang

def index(request) :

    if 'user_id' in request.session:

        tabel  = tabelSidang.objects.all()
        dictionary = {
            'dataSidang'   : tabel
        }
        return render(request, 'sidang/index.html', dictionary)
    
    else:
        return redirect('../')    

def tambah(request) :

    form = formSidang()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formSidang(request.POST, request.FILES)

        # VALIDASI FORM
        if form.is_valid():

            form.save()

            return redirect('../')

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


