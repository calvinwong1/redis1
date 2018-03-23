from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_redis(request):
    request.session['username']='django'
    request.session['password']=123456
    return HttpResponse("保存成功")


def get_redis(request):
    user = request.session.get('username')
    psw = request.session.get('password')
    text = 'username:%s  password:%s' % (user,psw)
    return HttpResponse(text)