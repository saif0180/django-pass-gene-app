from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'pas_gen/home.html')
def password(request):

    charcters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charcters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        charcters.extend('!@#$%^&*()')
    if request.GET.get('numbers'):
        charcters.extend('1234567890')

    length = int(request.GET.get('length',12))
    if length > 14:
        raise Exception('Make it 14 or less than 14')
    elif length < 6:
        raise Exception('Make it 6 or bigger than 6')
    thepassword = ''
    for x in range(length):
        thepassword +=random.choice(charcters)

    return render(request, 'pas_gen/password.html', {'password':thepassword})
def about(request):
    return render(request, 'pas_gen/about.html')
