import datetime as dt
from django.db import models
from django.db.models.signals import pre_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
#from django.dispatch import signals

# Create your models here.

class urlParseTimeshift(models.Model):
	url = models.URLField('URL', max_length=500)
	time_delay_minutes = models.IntegerField(default=0, help_text='>0', validators=[MinValueValidator(0, 'value < 0')])
	time_delay_seconds = models.IntegerField(default=0, help_text='0-59', validators=[MinValueValidator(0, 'value < 0'), MaxValueValidator(59, 'value > 59')])
	start_time = models.DateTimeField('Start time UTC', default = None)
	status_executed = models.BooleanField('Executed', default=False)
	status_success = models.BooleanField('Success', default=False)
	response_code = models.IntegerField(default=0)
	response_title = models.CharField('Title', max_length=500, default='')
	response_charset = models.CharField('charset', max_length=20, default='')
	response_h1 = models.CharField('h1', max_length=500, default='')

	def __str__(self):
		return self.url

	def save(self, *args, **kwargs):
		time_delay = dt.timedelta(minutes=self.time_delay_minutes) + dt.timedelta(seconds=self.time_delay_seconds)
		self.start_time = timezone.now() + time_delay
		if 'status_executed' in kwargs:			# при исполнении запроса сохраняем как исполненный
			self.status_executed = kwargs['status_executed']
		else:									# или при обновлении записи в бд сбрасываем на умолчания
			self.status_executed = False
			self.status_success = False
			self.response_code = 0
			self.response_title = ''
			self.response_charset = ''
			self.response_h1 = ''

		super(urlParseTimeshift, self).save()
