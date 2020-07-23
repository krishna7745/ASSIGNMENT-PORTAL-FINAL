from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
# Create your views here.
def dash(request):
    a=[]
    b=[]
    regis= apps.get_model('login', 'regis')
    ques= apps.get_model('login', 'ques')
    try:
        enroll=request.POST['enroll']
        ob=regis.objects.get(enroll=enroll)
        if ob.enroll:
            if ob.password==request.POST['passw']:
                 #a=[ob.q1,ob.q2,ob.q3,ob.q4,ob.q5,ob.q6,ob.q7,ob.q8,ob.q9,ob.q10]
                 sem=ob.sem;
                 name=ob.name
                 q=ques.objects.filter(sem=sem).values('quesno')
                 #b=q=ques.objects.filter(sem=sem,quesno=i).values('ques')
                 test=regis.objects.get(enroll=request.POST['enroll'])
                 for i in q:
                    a.append(ques.objects.filter(sem=sem,quesno=i['quesno']).values()[0])
                    b.append(i['quesno'])
                 return render(request,'dashboard.html',{'b':b ,'a':a,'enroll':enroll,'name':name,'sem':sem})
    except:
        return HttpResponse('<p style="background-color:lightblue;text-align:center;height:100"><i>NOT REGISTERED</i></p>')
