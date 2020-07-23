from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.
@csrf_exempt
def questions(request):
    enroll=request.POST['enroll']
    regis=apps.get_model('login', 'regis')
    ques=regis.objects.get(enroll=enroll)
    sem=ques.sem
    qno=[]
    for i in range(1,8):
        if(not eval('ques.q%d'%i)):
            qno.append(i)
    ques=apps.get_model('login', 'ques')
    q=ques.objects.filter(sem=sem).values()
    a={}
    for i in q:
        if i['quesno'] in qno:
            a[i['quesno']]=i['ques']
    return JsonResponse(a)