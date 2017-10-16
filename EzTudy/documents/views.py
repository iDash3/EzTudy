# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, School

from .forms import DocumentForm

def index(request):
	args = {}
	if request.method == 'POST':
		sc_id = request.POST.get('sc_id')
		# return redirect('/school/{}'.format(sc_id))
		return HttpResponseRedirect(reverse('documents:mainsc',args=(sc_id,)))

	schools = School.objects.order_by('id')
	context = {
		'school': schools
	}
	return render(request, 'index.html', context)

def success(request):
	return render(request, 'file_success.html', {})

def mainsc(request, sc_id):
	if request.GET.get('action') == 'ask':
		print('Ask')
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			d = form.save()
			d.save()
			return HttpResponseRedirect('/success')
	else:
		form = DocumentForm()

	school = get_object_or_404(School, pk=sc_id)
	context = {
		'school': school,
		'form': form,
	}
	return render(request, 'main.html', context)

# class DetailView(generic.DetailView):
# 	model = School
# 	template_name = 'main.html'

def worldsc(request):
	worldsc = School.objects.order_by('id',)
	return render(request, 'worldsc.html', {'world': worldsc})

def text_tm(request):
	context = {}
	return render(request, 'tc_ez.html', context)

def text_tc(request):
	return render(request, 'tc_ez.html', {})
def text_ua(request):
	return render(request, 'tc_ez.html', {})