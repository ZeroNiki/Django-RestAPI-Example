from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    discription = models.CharField(max_length=300, blank=True)
    date = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
