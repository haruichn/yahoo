from django.db import models
from django.contrib.auth.models import User

class Center(models.Model):
	place = models.CharField(max_length=200)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	age = models.IntegerField()
	center = models.ForeignKey(Center)
	sex = models.BooleanField()


