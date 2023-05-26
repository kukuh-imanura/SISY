import hashlib
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelYudisium
from . forms import formYudisium

def index(request) :

    if 'user_id' in request.session:
        tabel  = tabelYudisium.objects.all()
        dictionary = {
            'dataYudisium'   : tabel
        }
        return render(request, 'yudisium/index.html', dictionary)
    else:
        return redirect('../')



def tambah(request) :

    form = formYudisium()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formYudisium(request.POST, request.FILES)

        # VALIDASI FORM
        if form.is_valid():

            form.save()

            return redirect('../')

    return render(request, 'yudisium/tambah.html', dictionary)

def update(request, id_yudisium) :

    instance_yudisium = get_object_or_404(tabelYudisium, id_yudisium=id_yudisium)

    if request.method == 'POST':
        form = formYudisium(request.POST, request.FILES, instance=instance_yudisium)
        if form.is_valid():

            form.save()

            return redirect('../../')
    else:
        form = formYudisium(instance=instance_yudisium)

    dictionary  = {
        'dataForm'      : form,
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


