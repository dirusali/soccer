
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup, Jornada

from lxml import html
import requests
import json
import time

urls  = [
    'https://www.jornadaperfecta.com/partido/2521/girona-athletic',
    'https://www.jornadaperfecta.com/partido/2518/getafe-leganes',
    'https://www.jornadaperfecta.com/partido/2516/barcelona-espanyol',
    'https://www.jornadaperfecta.com/partido/2517/celta-villarreal',
    'https://www.jornadaperfecta.com/partido/2519/alaves-atletico',
    'https://www.jornadaperfecta.com/partido/2522/levante-eibar',
    'https://www.jornadaperfecta.com/partido/2525/rayo-vallecano-betis',
    'https://www.jornadaperfecta.com/partido/2520/sevilla-valencia',
    'https://www.jornadaperfecta.com/partido/2524/valladolid-real-sociedad',
    'https://www.jornadaperfecta.com/partido/2523/real-madrid-huesca']
    
    
    
    
actual= 246112 + 28*10

class Command(BaseCommand):
    def handle(self, *args, **options):
        actuales = (actual, actual+10)
        print('LA JORNADA ACTUAL VA DEL PARTIDO %s al %s' % (actual,actual+10))
        count = 0
        for i in range(actual,actual+10):
            try:
                p = Match.objects.get(matchid=i)
                local = p.local.name
                visitante = p.visitor.name
                match = ('%s - %s' % (local,visitante))
                count+=1
                url = urls[count-1]
                response = requests.get(url, timeout=10).text
                parser = html.fromstring(response)
                a = parser.xpath("//a['Player']")
                jugadores = []
                for i in a:
                    if i is not None:
                        jugadores.append(i.text)
                players = []
                for j in jugadores:
                    if j is not None:
                        if j != 'Contacto':
                            if 'Jornada' not in j:
                                if 'Cronista' not in j:
                                    if 'Aviso' not in j:
                                        players.append(j)  
            except Exception as e:
                print(e)
                pass
            
            try:
                playerlocales = players[:11]
                print('LOS JUGADORES LOCALES SON %s' % playerlocales)
                playersvisitantes=playerlocales[12:]
                print('LOS JUGADORES VISITANTES SON %s' & playersvisitantes)
                
                local_lineupid = '' 
                for p in playerlocales:
                    try:
                        q = Player.objects.filter(words__iexact=p) 
                        encontrado = (q[0])
                        local_lineupid += encontrado.name
                    except Exception as e:
                        palabras = p.split()
                        print(palabras)
                        for z in palabras:
                            print('buscando %s' % p)
                            q = Player.objects.filter(words__icontains=z)
                            for x in q:
                                print(x)
                                if x.team.name == local:
                                    encontrado = (q[0].words)
                                    local_lineupid += encontrado.name
                                    print('buscamos %s y encontramos %s' %(i, encontrado))
   
                                    
                visitor_lineupid = '' 
                for p in visitorlocales:
                    try:
                        q = Player.objects.filter(words__iexact=p) 
                        encontrado = q[0]
                        print('ENCONTRADO %s' % encontrado)
                        local_lineupid += encontrado.name
                    except Exception as e:
                        palabras = p.split()
                        print(palabras)
                        for z in palabras:
                            print('buscando %s' % p)
                            q = Player.objects.filter(words__icontains=z)
                            for x in q:
                                print(x)
                                if x.team.name == local:
                                    encontrado = (q[0].words)
                                    local_lineupid += encontrado.name
                                    print('buscamos %s y encontramos %s' %(i, encontrado))

            except Exception as e:
                print(e)
                pass   

   
            
