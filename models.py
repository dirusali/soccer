from django.core.exceptions import MultipleObjectsReturned
from django.db import models, OperationalError
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
import json
from django.utils import timezone
from model_utils.models import TimeStampedModel
from lxml import html
import collections
import logging
from django.db.models import Count
from django.urls import reverse
logger = logging.getLogger(__name__)
from datetime import datetime
from django.template.defaultfilters import truncatechars

class Competition(models.Model):
    name = models.CharField(max_length=500, blank=True)
    season
    
class Season(models.Model):
    years = models.CharField(max_length=500, blank=True)
    matches
    
class Match(models.Model):
    match = models.CharField(max_length=500, blank=True)
    home = models.CharField(max_length=500, blank=True)
    visitor= models.CharField(max_length=500, blank=True)
    phome = models.IntegerField(blank=True)
    pvisitor = models.IntegerField(blank=True)
    ghome = models.IntegerField(blank=True)
    gvisitor = models.IntegerField(blank=True)
    result = models.IntegerField(blank=True)
    alineacionhome =
    alineacionvisitor =
    
class Team(models.Model):
    name =
    player = 
    points =
    gf = 
    gc =
    pg =
    pe =
    pp =
    alineacion1
    ali2
    ....
    
    
    
