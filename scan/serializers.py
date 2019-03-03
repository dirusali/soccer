from rest_framework import serializers
from scan.models import Team, Match

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer(required = False)
    class Meta:
        model = Team
        fields = '__all__'

class MatchSerializer(serializers.HyperlinkedModelSerializer):  
    match = MatchSerializer(required = False)

    class Meta:
        model = Match
        fields = '__all__'
