from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=210, null=False)
    text = models.CharField(max_length=500, null=False)
    author = models.CharField(max_length=210, null=False)

    def __str__(self):
        return self.title


