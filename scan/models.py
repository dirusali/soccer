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

class Player(models.Model):
    name = models.CharField(max_length=500, blank=True)
   
class Lineup(models.Model):
    name = models.CharField(max_length=500, blank=True)
    players = models.ManyToManyField(Player, blank=True, related_name='lineup')
    
class Team(models.Model):
    name = models.CharField(max_length=500, blank=True)
    lineups = models.ManyToManyField(Lineup, blank=True, related_name='team')
    points = models.IntegerField(blank=True)
    matches_won = models.IntegerField(blank=True)
    matches_tied = models.IntegerField(blank=True)
    matches_lost= models.IntegerField(blank=True)
    
class Match(models.Model):
    teams = lineups = Models.ManyToManyField(Team, blank=True, related_name='match')
    matchday = models.IntegerField(blank=True)
    #local = models.ForeignKey(Team)
    #visitor = models.ForeignKey(Team)
    #plocal = models.ForeignKey(Team)
    #pvisitor = models.ForeignKey(Team)
    #ghome = models.IntegerField(blank=True)
    #gvisitor = models.IntegerField(blank=True)
    #result = models.IntegerField(blank=True)
    #lineuphome = models.Foreign(max_length=500, blank=True)
    #lineupvisitor = models.Foreign(max_length=500, blank=True)


class Competition(models.Model):
    name = models.CharField(max_length=500, null =True, blank=True)
    match = models.ForeignKey(Match)

    
    
    
    
    
    

