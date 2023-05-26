from django.shortcuts import render, redirect

def index(request) :

    if 'user_id' in request.session:

        return render(request, 'index.html')
    
    else:
        return redirect('login/')