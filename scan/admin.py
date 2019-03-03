from scan.models import Competition, Match, Team, Player


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'season')
    search_fields = ('name',)

admin.site.register(Competition, CompetitionAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('match', 'matchday', 'local', 'visitor')
    list_filter = ('local,)
    
admin.site.register(Macth, MacthAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
    list_filter = ('name',)

admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Player, PlayerAdmin)
