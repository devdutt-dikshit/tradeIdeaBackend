from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime


class Crypto(models.Model):
    cryptoName = models.CharField(max_length=30)
    def __str__(self): 
        return self.cryptoName

class TradeIdea(models.Model):
    tradeType = models.CharField(max_length=10)
    ideaName = models.CharField(max_length=50)
    crypto = models.ForeignKey(Crypto, on_delete= models.CASCADE)
    risk = models.CharField(max_length=20)
    target = models.IntegerField()
    stopLoss= models.IntegerField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribedBy = models.TextField()
    createdAt= models.TimeField(default=datetime.now)
    def __str__(self): 
        return self.ideaName

class Subscribe(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    tradeIdeaId = models.ForeignKey(TradeIdea, on_delete=models.CASCADE)


