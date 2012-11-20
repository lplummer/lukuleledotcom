from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=100, blank=True)
	date = models.DateField(auto_now_add=True)
	content = models.TextField()
	def __unicode__(self):
		return "{}, {}".format(self.title, self.date)