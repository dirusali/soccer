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

class Competition(models.Model):
    name = models.CharField(max_length=500, null =True, blank=True)
    match = models.CharField(max_length=500, null =True, blank=True)
    season = models.CharField(max_length=500, null =True, blank=True)

    
class Match(models.Model):
    match = models.ForeignKey(Competition)
    matchday = models.IntegerField(Competition)
    season = models.CharField(max_length=500, blank=True)
    local = models.ForeignKey(Team)
    visitor = models.ForeignKey(Team)
    #plocal = models.ForeignKey(Team)
    #pvisitor = models.ForeignKey(Team)
    ghome = models.IntegerField(blank=True)
    gvisitor = models.IntegerField(blank=True)
    result = models.IntegerField(blank=True)
    #lineuphome = models.Foreign(max_length=500, blank=True)
    #lineupvisitor = models.Foreign(max_length=500, blank=True)

    
class Team(models.Model):
    name = models.CharField(max_length=500, blank=True)
    player = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)
    gf = models.IntegerField(blank=True)
    gc = models.IntegerField(blank=True)
    pg = models.IntegerField(blank=True)
    pe = models.IntegerField(blank=True)
    pp = models.IntegerField(blank=True)
    #lineup = models.CharField(max_length=500, blank=True)

class Player(models.Model):
    name = models.CharField(max_length=500, blank=True)
    
    
    
    
    
    

