from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout


from . forms import formLogin
from mahasiswa.models import tabelMhs

def index(request):
    if request.method == 'POST':

        form = formLogin(request.POST)

        if form.is_valid():
            
            # Ambil data yang diisi oleh pengguna
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                mhs = tabelMhs.objects.get(username=username, password=password)
                if mhs.username == username and mhs.password == password:

                    request.session['user_id'] = mhs.nim
                    request.session['username'] = mhs.username

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
    logout(request)
    return redirect('../')
