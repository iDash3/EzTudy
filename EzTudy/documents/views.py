# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.http import HttpResponse

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, School
# Create your views here.

def index(request):
	args = {}
	if request.method == 'POST':
		sc_id = request.POST.get('sc_id')
		# args['sc_id'] = sc_id
		return redirect('/school/{}'.format(sc_id))
		# return redirect(reverse('/school/',args=(sc_id,)))

	schools = School.objects.order_by('id')
	context = {
		'school': schools
	}
	return render(request, 'index.html', context)

def mainsc(request, sc_id):
	school = get_object_or_404(School, pk=sc_id)
	return render(request, 'main.html', {'school': school})

def worldsc(request):
	worldsc = School.objects.order_by('id',)
	return render(request, 'worldsc.html', {'world': worldsc})

def text_tm(request):
	context = {}
	return render(request, 'tc_ez.html', context)