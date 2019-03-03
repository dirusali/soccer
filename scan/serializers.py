from rest_framework import serializers
from scan.models import 

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MatchSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Match
        fields = '__all__'
