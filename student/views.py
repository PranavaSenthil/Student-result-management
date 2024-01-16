from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render
from .models import year,subject,student,result
from .forms import yearform,subjectform,studentform,resultform
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def vr(request):
   return render(request,'studentid.html')

def sr(request):
   if request.method == 'POST':
      student_id = request.POST.get('student_id')
      sems = result.objects.filter(student_ID=student_id)
      context = {'sems':sems}
   return render(request,'sr.html',context)

def login(request):
  if request.method == 'POST':  
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('dash')
    else:
        messages.info(request,'Invalid username or password')
        return redirect('login')
  else:
    return render(request,'login.html')
  
def logout(request):
   auth.logout(request)
   return redirect('home')

def dash(request):
   semester_len = year.objects.count()
   subject_len = subject.objects.count()
   student_len = student.objects.count()
   result_len = result.objects.count()
   context={"semester_len":semester_len,'subject_len':subject_len,'student_len':student_len,'result_len':result_len}
   return render(request,'dash.html',context)

def semester(request):
   forms = yearform()
   if request.method == 'POST':
      forms = yearform(request.POST)
      if forms.is_valid():
         forms.save()
   sems = year.objects.all()
   context = {'forms':forms,'sems':sems}
   return render(request,'semester.html',context)

def edit(request,id):
   seme= year.objects.get(Sno=id)
   forms = yearform(instance=seme)
   if request.method == 'POST':
      forms = yearform(request.POST,instance=seme)
      if forms.is_valid():
         forms.save()
         return redirect('semester')
   sems = year.objects.all()
   context = {'forms':forms,'sems':sems,'seme':seme}
   return render(request,'edit.html',context)

def delete(request,id):
    con = year.objects.get(id=id)
    con.delete()
    return redirect('semester')

def subjects(request):
   forms = subjectform()
   if request.method == 'POST':
      forms = subjectform(request.POST)
      if forms.is_valid():
         forms.save()
   sems = subject.objects.all()
   context = {'forms':forms,'sems':sems}
   return render(request,'subject.html',context)

def edits(request,id):
   seme= subject.objects.get(id=id)
   forms = subjectform(instance=seme)
   if request.method == 'POST':
      forms = subjectform(request.POST,instance=seme)
      if forms.is_valid():
         forms.save()
         return redirect('subjects')
   sems = subject.objects.all()
   context = {'forms':forms,'sems':sems,'seme':seme}
   return render(request,'edit1.html',context)

def deletes(request,id):
    con = subject.objects.get(id=id)
    con.delete()
    return redirect('subjects')

def students(request):
   forms = studentform()
   if request.method == 'POST':
      forms = studentform(request.POST)
      if forms.is_valid():
         forms.save()
   sems = student.objects.all()
   context = {'forms':forms,'sems':sems}
   return render(request,'student.html',context)

def editss(request,id):
   seme= student.objects.get(Sno=id)
   forms = studentform(instance=seme)
   if request.method == 'POST':
      forms = studentform(request.POST,instance=seme)
      if forms.is_valid():
         forms.save()
         return redirect('students')
   sems = student.objects.all()
   context = {'forms':forms,'sems':sems,'seme':seme}
   return render(request,'edit2.html',context)

def deletess(request,id):
    con = student.objects.get(Sno=id)
    con.delete()
    return redirect('students')

def results(request):
   forms = resultform()
   if request.method == 'POST':
      forms = resultform(request.POST)
      if forms.is_valid():
         forms.save()
   sems = result.objects.all()
   context = {'forms':forms,'sems':sems}
   return render(request,'result.html',context)

def eds(request,id):
   seme = result.objects.get(Sno=id)
   forms = resultform(instance=seme)
   if request.method == 'POST':
      forms = resultform(request.POST,instance=seme)
      if forms.is_valid():
         forms.save()
         return redirect('results')
   sems = result.objects.all()
   context = {'seme':seme,'forms':forms,'sems':sems}
   return render(request,'eds.html',context)

def dels(request,id):
    con = result.objects.get(Sno=id)
    con.delete()
    return redirect('results')