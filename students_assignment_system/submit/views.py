import json
import requests
from django.shortcuts import render
from django.apps import apps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def sub(request):
    response=False
    regis=apps.get_model('login','regis')
    ques=apps.get_model('login','ques')
    code=request.POST['code']
    enroll=request.POST['enroll']
    quesno=int(request.POST['quesno'])
    sem=request.POST['sem']
    input=request.POST['input']
    output=request.POST['output']
    print(input,output)
    print(input,output)
    code=json.loads(code)
    input=json.loads(input)
    url="https://ide.geeksforgeeks.org/main.php"
    data={
        'lang': 'C',
        'code':code,
        'input': input,
        'save': 'false'
    }
    req=requests.post(url,data)
    req=json.loads(req.text)
    d={'sid':req['sid'],'requestType': 'fetchResults'}
    url="https://ide.geeksforgeeks.org/submissionResult.php"
    req=requests.post(url,d)
    req=json.loads(req.text)
    print(req)
    while req['status']== 'IN-QUEUE':
        req=requests.post(url,d)
        req=json.loads(req.text)
        print(req)
    if str(req["output"])==str(output):
        res=regis.objects.get(enroll=enroll)
        one=1
        q=exec('res.q%d=one'% quesno)
        #print(q)
        res.save()
        response=True
    return JsonResponse({'response':response})
