from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
	title = models.CharField(max_length=100, blank=True)
	date = models.DateField(auto_now_add=True)
	content = models.TextField()
	author = models.ForeignKey(User, related_name='blogposts')
	def __unicode__(self):
		return "{}, {} by {}".format(self.title, self.date, self.author)