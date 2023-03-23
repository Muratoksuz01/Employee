from django.shortcuts import render,redirect
from .models import ModelEmployee
from .forms import FormEmployee
from django.contrib.auth import authenticate
# Create your views here.
def index(request):#create
    if request.method=="POST":
        form=FormEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste")
    form=FormEmployee()
    return render(request,"base/index.html",{"form":form})
def liste(request):
    form=ModelEmployee.objects.all()
    return render(request,"base/list.html",{"forms":form})
def edit(request,pk):
    employee=ModelEmployee.objects.get(id=pk)
    form=FormEmployee(instance=employee)

    return render(request,"base/index.html",{"form":form})
def delete(request,pk):
    form=ModelEmployee.objects.get(id=pk)
    form.delete()
    return redirect("liste")
