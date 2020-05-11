from django.http import HttpResponse
from django.shortcuts import render
from .models import generate
from django.utils import timezone
import secrets


def index(request):
    return render(request,'index.htm')
def kyukey(request):
    secretsgen=secrets.SystemRandom()
    otp=secretsgen.randrange(1000,9999)
    val=otp
    x = generate(key = otp)
    x.save()
    return render(request,'index.htm',{'gen':val})