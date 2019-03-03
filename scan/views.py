from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from .models import Competition, Match, Team, Player
from .serializers import MatchSerializer, TeamSerializer

#class MatchFilter(filters.FilterSet):
#    matchday = filters.CharFilter(lookup_expr=['icontains','exact', 'iexact'])
#    local = filters.CharFilter(lookup_expr=['icontains','exact', 'iexact'])
#    visitor = filters.CharFilter(lookup_expr=['icontains','exact', 'iexact'])
#    class Meta:
#        model = Match
#        fields = ['match', 'match', 'matchday', 'local', 'visitor']
        
class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Products to be viewed.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
   # filter_class = MatchFilter
    search_fields = ('match', 'matchday', 'local', 'visitor')

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Shop to be viewed.
    """
    queryset = Team.objects.all()
    serializer_class = Teamserializer
