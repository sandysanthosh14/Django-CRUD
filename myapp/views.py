from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import Studentform

# Create your views here.
def form(request):
    details=Student.objects.all()
    return render(request,'myapp/index.html',context={'student':details})
def create(request):
    stu=Studentform()
    if request.method=='POST':
        stu=Studentform(request.POST)
        if stu.is_valid():
            stu.save()
            return redirect('/index')
    return render(request,'myapp/form.html',context={'stu':stu})
def stu_delet(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/index')
def update_view(request,id):
    s=Student.objects.get(id=id)
    if request.method=='POST':
        stu=Studentform(request.POST,instance=s)
        if stu.is_valid():
            stu.save()
            return redirect('/index')
    return render(request,'myapp/update.html',context={'stu':s})



