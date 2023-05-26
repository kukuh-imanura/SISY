import hashlib
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelMhs
from . forms import formMhs

def index(request) :

    if 'user_id' in request.session:

        tabel  = tabelMhs.objects.all()
        dictionary = {
            'dataMahasiswa'   : tabel
        }
        return render(request, 'mahasiswa/index.html', dictionary)
    
    else:
        return redirect('../')

def tambah(request) :

    form = formMhs()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formMhs(request.POST)

        # VALIDASI FORM
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            petugas = form.save(commit=False)

            # AMBIL DATA PASSWORD
            password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # MENGEMBALIKAN DATA PASSWORD
            petugas.password = hashed_password

            # SMPAN PASSWORD
            petugas.save()

            return redirect('../')

    return render(request, 'mahasiswa/tambah.html', dictionary)

def update(request, nim_mhs) :

    instance_mhs = get_object_or_404(tabelMhs, nim=nim_mhs)

    if request.method == 'POST':
        form = formMhs(request.POST, instance=instance_mhs)
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            save_mhs = form.save(commit=False)

            # AMBIL DATA PASSWORD
            password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # MENGEMBALIKAN DATA PASSWORD
            save_mhs.password = hashed_password

            # SMPAN PASSWORD
            save_mhs.save()

            return redirect('../../')
    else:
        form = formMhs(instance=instance_mhs)

    dictionary  = {
        'dataForm'      : form,
        'dataMahasiswa' : instance_mhs,
    }

    return render(request, 'mahasiswa/update.html', dictionary)

def hapus(request, nim_mhs):

    instance_mhs = get_object_or_404(tabelMhs, nim=nim_mhs)

    if instance_mhs.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'mahasiswa/index.html', dictionary)


