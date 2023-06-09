from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
import hashlib


from . forms import formLogin
from mahasiswa.models import tabelMhs
from petugas.models import tabelPetugas

def index(request):
    if request.method == 'POST':

        form = formLogin(request.POST)

        if form.is_valid():
            
            # Ambil data yang diisi oleh pengguna
            username = form.cleaned_data['username']
            # AMBIL DATA PASSWORD
            password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            try:
                petugas = tabelPetugas.objects.get(username=username, password=hashed_password)
                if petugas.username == username and petugas.password == hashed_password :

                    if petugas.tipe == 'fakultas' :
                        request.session['petugas_fakultas'] = petugas.nidn
                        request.session['nama'] = petugas.nama

                        return redirect('../')
                    else :
                        request.session['petugas_prodi'] = petugas.nidn
                        request.session['nama'] = petugas.nama

                        return redirect('../')
                    
                else:
                    messages.error(request, 'Username atau Password Salah')
            except tabelPetugas.DoesNotExist:
                try:

                    mhs = tabelMhs.objects.get(username=username, password=hashed_password)
                    if mhs.username == username and mhs.password == hashed_password:

                        request.session['mhs_id'] = mhs.nim
                        request.session['nama'] = mhs.nama

                        return redirect('../')
                    else:
                        messages.error(request, 'Username atau Password Salah')
                except tabelMhs.DoesNotExist:
                    messages.error(request, 'Akun tidak ditemukan')

    else:
        form = formLogin()

    context = {
        'dataForm': form
    }
    
    return render(request, 'login/index.html', context)

def logout_view(request):
    # Membersihkan semua kunci dalam session
    request.session.clear()
    # Menghancurkan sesi
    request.session.flush()
    # Melakukan logout pengguna
    logout(request)
    return redirect('../')
