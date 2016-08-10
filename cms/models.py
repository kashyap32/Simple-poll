from __future__ import unicode_literals


import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.






class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# ...
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	# ...
	def __str__(self):
		return self.choice_text

class UserDetail(models.Model):
	user = models.ForeignKey(User)
	#poll = models.ForeignKey(Question)
	phone_number = models.BigIntegerField(null= True)


	def __unicode__(self):
		return self.user.username
