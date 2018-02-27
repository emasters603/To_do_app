# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task
from django.template import loader
# Create your views here.

def index(request):
	task_list = Task.objects.all()_
	conext = {'task_list': task_list}
	return render(request, to_do_app/index.html, context)

def detail(request, ID):
	try:
		task_list = Task.objects.get(pk=ID)
	except Task.Doesnotexist
		raise Http404('There are not that many tasks')
	context = {'task' : task,}
	return render(request, 'to_do_app/detail.html', context)
	
