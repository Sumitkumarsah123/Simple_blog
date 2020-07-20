from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.
class Blog(models.Model):

    title= models.CharField(max_length=100)
    writer=models.CharField(max_length=20)
    content= models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    


    # ask to senior

    class Admin:
        list_display = ('title', 'writer', 'date_posted') 
    list_filter = ('writer', 'date_posted') 
    ordering = ('-date_posted',) 
    search_fields = ('title',)


TOPIC_CHOICES=(
    ('general', 'general enquiry'),
    ('bug', 'bug report'),
    ('suggestion', 'suggestion'),

)

class Feedback(models.Model):

    topic = models.CharField(max_length=50) 
    message=models.TextField()
    sender = models.EmailField()






