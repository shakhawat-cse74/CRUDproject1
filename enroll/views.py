from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentsRegistration
from .models import User

# Create your views here.

# This Function for Add and show Data
def show_data(request):
    if request.method == 'POST':
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentsRegistration()
    else:
        fm = StudentsRegistration()
    stud = User.objects.all()
    return render (request, 'enroll/addandshow.html',{'form':fm, 'std':stud})


#This Function For Update/Edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentsRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentsRegistration(instance=pi)
    return render (request,'enroll/updatedata.html', {'form':fm})

# This Function For Delete data
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')