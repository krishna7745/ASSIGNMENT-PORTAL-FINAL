from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
import requests
import json


@csrf_exempt
# @api_view(['POST'])
# @parser_classes([JSONParser])
def api(request):
    res = []
    code = request.POST['code']
    input = (request.POST['input'])
    input = json.loads(input)
    code = json.loads(code)
    url = "https://ide.geeksforgeeks.org/main.php"
    data = {
        'lang': 'C',
        'code': code,
        'input': input,
        'save': 'false'
    }
    print(input)
    req = requests.post(url, data)
    req = json.loads(req.text)
    d = {'sid': req['sid'], 'requestType': 'fetchResults'}
    url = "https://ide.geeksforgeeks.org/submissionResult.php"
    req = requests.post(url, d)
    req = json.loads(req.text)
    print(req)
    while req['status'] == 'IN-QUEUE':
        req = requests.post(url, d)
        req = json.loads(req.text)
        print(req)
    return JsonResponse(req)
