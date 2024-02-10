from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=277)

    def __str__(self):
        return str(self.id)
