from django.db import models
from django.forms import ModelForm

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    sender = models.EmailField()
    def __unicode__(self):
        return self.sender

class ContactForm(ModelForm):
    class Meta:
        model = Contact
