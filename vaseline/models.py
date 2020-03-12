from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.

class Sett(models.Model):
    name=models.CharField(max_length=40)
    question_number=models.IntegerField()
    uuid=models.UUIDField( primary_key = True, 
         default = uuid.uuid4, 
         editable = True)
    users = models.ManyToManyField(User,blank=True)
    pubdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['name']

class Question(models.Model):
     name=models.CharField(max_length=40)
     description=models.TextField()
     output_template=models.TextField()
     sett= models.ForeignKey(Sett, on_delete=models.CASCADE)


class Answer(models.Model):
    ans=models.TextField()
    right=models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)