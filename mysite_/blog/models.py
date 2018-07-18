from django.db import models
from django.utils import timezone #다른파일에 있는것을 추가하라


class Post(models.Model): #post라는 모델을 정의
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

#__str__ : admin 표시
    def __str__(self):
        return self.title


class Tour(models.Model):
	nation = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	who = models.CharField(max_length=200)
	to_date = models.DateTimeField()
	from_date = models.DateTimeField()
	comment = models.TextField()

	def __str__(self) :
		return self.from_date + "~" + self.to_date + "(" + self.nation + ")"

