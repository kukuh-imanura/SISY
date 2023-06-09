from django.shortcuts import render, redirect

def index(request) :

    if 'petugas_fakultas' in request.session or 'petugas_prodi' in request.session or 'mhs_id' in request.session:
        
        context = {
            'nama'  : request.session['nama']
        }

        return render(request, 'index.html', context)
    
    else:
        return redirect('login/')