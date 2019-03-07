from django.core.exceptions import MultipleObjectsReturned
from django.db import models, OperationalError
import json
from django.utils import timezone
import logging
from django.db.models import Count
from django.urls import reverse
logger = logging.getLogger(__name__)
from datetime import datetime
from django.template.defaultfilters import truncatechars
    
class Team(models.Model):
    name = models.CharField(max_length=500, blank=True)
    identificador = models.IntegerField(null=True, blank=True)
    coach = models.CharField(max_length=500, null = True, blank=True)
   
class Player(models.Model):
    name = models.CharField(max_length=500, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    
class Lineup(models.Model):
    name = models.CharField(max_length=500, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    players = models.ManyToManyField(Player, blank=True, related_name='lineup')
    timeplayed = models.IntegerField(null=True,blank=True)
    goalsfavor = models.IntegerField(null=True,blank=True)
    goalscounter = models.IntegerField(null=True,blank=True)
      
class Match(models.Model):
    local = models.ForeignKey(Team, null=True, blank=True, related_name='localteam')
    visitor = models.ForeignKey(Team, null=True, blank=True, related_name='visitorteam')
    matchid = models.IntegerField(blank=True, null=True)
    
class Competition(models.Model):
    name = models.CharField(max_length=500, null =True, blank=True)

    
    
    
    
    
    

