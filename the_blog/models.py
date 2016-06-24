from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(User, default=1)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('blogpost-detail', kwargs={'pk':self.id})

    def __str__(self):
        return self.title
