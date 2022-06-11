from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=True)
  
    class Meta():
        ordering = ["-created_on"]


    def __str__(self):
        return self.title
        return self.created_on

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

