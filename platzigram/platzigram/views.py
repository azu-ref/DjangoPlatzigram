#django
from django.http import HttpResponse
from django.http import JsonResponse
import json

#utilities
from datetime import datetime

def hello_world(request):
#return a greeting
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def sort_numbers(request):
    """Devuelve los numeros que le pasamos por parametro"""
    numbers = request.GET['numbers']
    #import pdb; pdb.set_trace()
    list_numbers= sorted(map(int ,numbers.split(',')))
    dic_numbers = {
        'status': 'OK',
        'numbers': list_numbers,
        'message': 'Numbers sorted successfully'
        }
    
    return HttpResponse(json.dumps(dic_numbers), content_type='application/json')

def say_hi(request, name, age):
    """return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are ot allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)

    return HttpResponse(message)