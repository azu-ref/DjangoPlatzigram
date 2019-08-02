#django
from django.http import HttpResponse
from django.http import JsonResponse

#utilities
from datetime import datetime

def hello_world(request):
#return a greeting
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def hi(request):
    """Devuelve los numeros que le pasamos por parametro"""
    numbers = request.GET['numbers']
    #import pdb; pdb.set_trace()
    # print(request.GET)
    # print(type(numbers))
    list_numbers= sorted(map(int ,numbers.split(',')))
    dic_numbers = {'numbers': list_numbers }
    
    return JsonResponse(dic_numbers)