from django.db import models
from django.utils import timezone #다른파일에 있는것을 추가하라


class Post(models.Model): #post라는 모델을 정의
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
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
    nation = models.TextField()
    city = models.TextField()
    who = models.TextField()
    to_date = models.DateTimeField()
    from_date = models.DateTimeField()
    comment = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(blank=True,upload_to='%Y/%m/%d/filtered')
    created_at = models.DateTimeField(auto_now_add=True)
    background_color=models.TextField(default='white')
    font_color=models.TextField(default='black')
    def __str__(self) :
        return self.nation 