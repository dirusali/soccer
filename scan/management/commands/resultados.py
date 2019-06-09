from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json

url = 'http://api.football-data.org/v2/competitions/2014/teams?season=2016'


class Command(BaseCommand):
    def handle(self, *args, **options):
