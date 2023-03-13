from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


'''
    def comment(self, name, email, comment ):

        Comment.objects.create(post=self, name=name, email=email, comment=comment)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone)'''

