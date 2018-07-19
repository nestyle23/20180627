from django.db import models
from django.utils import timezone #다른파일에 있는것을 추가하라


class Tour(models.Model):
	nation = models.TextField(max_length=200)
	city = models.TextField(max_length=200)
	who = models.TextField(max_length=200)
	to_date = models.DateTimeField()
	from_date = models.DateTimeField()
	comment = models.TextField()
	image = models.ImageField(upload_to='%Y/%m/%d/orig')
	filtered_image = models.ImageField(blank=True,upload_to='%Y/%m/%d/filtered') 
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) :
		return self.nation 

