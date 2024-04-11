from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# settings.AUTH_USER_MODEL 대신에 User 쓸수있음

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank = True,null= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    