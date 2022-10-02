from django.shortcuts import render
from .models import User
from .forms import StudentForm
from django.db.models import Q
# Create your views here.
def home(request): 
        if 'q' in request.GET:
            q=request.GET['q']
            # data = User.objects.filter(name__icontains=q)
            multiple_q=Q(Q(name__icontains=q) |Q(address__icontains=q))
            data=User.objects.filter(multiple_q)
        else:
          data=User.objects.all()
        context={
            'data':data
        }
        return render(request,"en/home.html",context)