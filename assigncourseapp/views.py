from django.shortcuts import render,redirect
from .models import course
from assigncourseapp.forms import courseform
# Create your views here.
def getcourse(request):
    course_obj=course.objects.all()
    return render(request,'assigncourseapp/course.html',{'courses':course_obj})
def createcourse(request):
    form=courseform()
    if request.method=='POST':
        form=courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'assigncourseapp/createcourse.html',{'form':form})
def deletecourse(request,id):
    courseobj=course.objects.get(id=id)
    courseobj.delete()
    return redirect('/')
def updatecourse(request,id):
    courseobj=course.objects.get(id=id)
    form=courseform(instance=courseobj)
    if request.method=='POST':
        form=courseform(request.POST,instance=courseobj)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'assigncourseapp/updatecourse.html',{'form':form})


