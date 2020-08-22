from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTextField

# Create your models here.

class PostProblem(models.Model):

	creator = models.ForeignKey(User, on_delete = models.CASCADE)
	# problem = RichTextField(blank=True, null= True)
	problem_title = models.TextField()
	image = models.ImageField(upload_to="images/")
	created_date = models.DateField(auto_now_add = True)
	location = models.CharField(max_length = 255)
	status = models.CharField(max_length = 100)
	# ?snippet = models.CharField(max_length= 255, default='See more..')
	likes = models.ManyToManyField(User, related_name='post_like')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.problem_title

	def get_absolute_url(self):
		return reverse('home')
	# 	return reverse('article-detail', args=(str(self.pk)))

class Comment(models.Model):
	post = models.ForeignKey(PostProblem, related_name='comments', on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.TextField()
	date_commented = models.DateField(auto_now_add = True)

	def __str__(self):
		return '%s - %s' % (self.post.problem_title, self.user)

	def get_absolute_url(self):
		return reverse('problem-detail', args=(str(self.post.pk)))
