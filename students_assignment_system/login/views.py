from django.shortcuts import render
from .models import regis
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.POST['enroll'] !="1":
        enroll=request.POST['enroll']
        name= request.POST['name']
        email=request.POST['email']
        password=request.POST['passw']
        course=request.POST['course']
        sem=request.POST['sem']
        ex=regis(enroll=enroll,name=name,email=email,password=password,course=course,sem=sem)
        ch=regis.objects
        a=0
        try:
            if enroll:
                print(enroll)
                ch=regis.objects.get(enroll=enroll)
                print(ch)
                a=ch.enroll
        except:
            if(not ex.save()):
                return render(request,'login.html')
            else:
                return HttpResponse("SOMETHING WENT WRONG")
        finally:
            if enroll == a:
                return HttpResponse('<p style="background-color:lightblue;text-align:center;height:100"><i>ALREADY REGISTERED</i></p>')
    return render(request, 'login.html')
