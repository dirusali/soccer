from scan.models import Competition, Match, Team, Player, Lineup
from django.contrib import admin


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)

admin.site.register(Competition, CompetitionAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ['matchid', 'local', 'visitor']
    list_filter = ('matchid',)
    
admin.site.register(Match, MatchAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'coach']
    list_filter = ('name',)

admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'age']
    list_filter = ('name',)

admin.site.register(Player, PlayerAdmin)

class LineupAdmin(admin.ModelAdmin):
    list_display = ['name', 'timeplayed', 'goalsfavor', 'goalscounter']
    raw_id_fields = ['players']
    
admin.site.register(Lineup, LineupAdmin)
