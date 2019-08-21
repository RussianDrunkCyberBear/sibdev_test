from . models import *
import requests
import re
import time
import threading
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

def sheduledParse():
	
	#while True:
	db_items = urlParseTimeshift.objects.filter(status_executed=False)	# неисполненные запросы
	
	for t in threading.enumerate():			# чтобы не дублировались таймеры очищаем
		if isinstance(t, threading.Timer):
			t.cancel()
	
	if db_items:
		for db_item in db_items:			
			delay = db_item.start_time - timezone.now()				
			delay = delay.total_seconds()
			db_item_timer = threading.Timer(delay, dealayedParse, args=(db_item,))			# каждый запрос запускается в отдельный тред с таймером
			db_item_timer.start()
			print(f'timer started {delay} - {db_item.url}')
		
		#time.sleep(2)


def dealayedParse(db_item):
	
	response = parserRequest(db_item.url)
	db_item.status_success = response['status_success']
	db_item.response_code = response['status_code']
	db_item.response_title = response['title']
	db_item.response_charset = response['charset']
	db_item.save(status_executed = True)
	print(f'{db_item.url}  - Executed')
	#print(f'{db_item.url} --- {db_item.start_time.strftime("%Y-%m-%d %H:%M:%S")} --- Executed: {db_item.status_executed}')


def parserRequest(url):
	
	response_dct = {'status_success':False,
					'status_code':0,
					'title':'',
					'charset':'',
					'h1':''}

	try:
		response = requests.get(url)
	except:		# если адреса не существует
		return response_dct

	response_dct['status_success'] = True
	response_dct['status_code'] = response.status_code

	if 'title' in response.text.lower():
		title = re.search(r'<title>(.*?)<\/title>', response.text, flags=re.IGNORECASE).group(1)
		response_dct['title'] = title
		#print(f'Title: {title}')
	if 'charset' in response.headers['Content-Type'].lower():
		charset = re.search(r'(?<=charset=).*\b', response.headers['Content-Type'], flags=re.IGNORECASE).group(0)
		response_dct['charset'] = charset
		#print(f'Encode: {charset}')
	if 'h1' in response.text.lower():
		h1 = re.search(r'(?<=h1>).*?(?=<\/h1>)', response.text, flags=re.IGNORECASE)
		#print(repr(h1))

	return response_dct



# сброс таймеров при изменении в базе

@receiver([post_save, post_delete], sender=urlParseTimeshift)

def sheduleReseter(sender, **kwargs):
	print('DB changed: shedule reset')
	sheduledParse()

