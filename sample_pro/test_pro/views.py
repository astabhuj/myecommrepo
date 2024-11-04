from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def additionView(r):
    #incoming = r.POST
    incoming = json.loads(r.body)
    print(incoming)
    out = int(incoming['x']) * int(incoming['y'])
    data = {'result':out}
    return JsonResponse(data)

