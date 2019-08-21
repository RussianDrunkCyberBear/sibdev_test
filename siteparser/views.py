from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from . models import *
import datetime as dt

def parse_results(request):
	db_items = urlParseTimeshift.objects.filter(status_executed=True)
	for db_item in db_items:
		db_item.f_start_time = db_item.start_time.strftime("%d.%m.%Y %H:%M:%S")
	return render(request, 'index.html', locals())