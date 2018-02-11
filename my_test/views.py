# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import User
# Create your views here.

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def list_user(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    return render(request,'list_user.html',context)

def new_user(request):
    return render(request, 'list_user.html', {})

def create_user(request):
    pass