from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm
from django.contrib.auth import login, authenticate

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Siz loginni muvaffaqiyatli amalga oshirdingiz!')
                else:
                    return HttpResponse('siz aktiv emassiz')
            else:
                return HttpResponse('Kechirasiz sizning login yoki parolingiz xato')
        else:
            return HttpResponse('Kechirasiz siz tuliq malumot kiritmagansiz!')

    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'registration/login.html', context)



def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'registration/dashboard.html', context)


