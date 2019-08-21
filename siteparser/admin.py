from django.contrib import admin
from django import forms

from .models import *


class UrlParseTimeshiftForm(forms.ModelForm):

	class Meta:
		model = urlParseTimeshift
		fields = ['url', 'time_delay_minutes', 'time_delay_seconds' ]
	
# Register your models here.

class UrlParseTimeshiftAdmin(admin.ModelAdmin):
	list_display = ('url', 'start_time', 'status_executed', 'status_success', 'response_code')
	readonly_fields = ['start_time', 'status_executed', 'status_success', 'response_code', 'response_title', 'response_h1']
	form = UrlParseTimeshiftForm
	
	class Meta:
		model = urlParseTimeshift

admin.site.register(urlParseTimeshift, UrlParseTimeshiftAdmin)
