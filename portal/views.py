import functools
import operator

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views import View
from django.db.models import Count

from scan.models import Lineup, Player,Team
from scan.serializers import SearchTagSearializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>HelloWorld</h1>")
