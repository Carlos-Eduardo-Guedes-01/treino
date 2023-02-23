from django.shortcuts import render,redirect
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from falcao.models import *
from accounts.models import *
from administrador.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def home_adm(request):
    user=request.user
    mode_user=User.objects.get(username=user)
    instalador_=admin.objects.get(usuario=mode_user.id)
    data={}
    data['nome']=instalador_.usuario.first_name
    if(user is None):
        return redirect('accounts:inicio')
    return render(request,'../../falcao/templates/home.html',data)