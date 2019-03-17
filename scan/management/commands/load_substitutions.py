from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json
from time import sleep

urlmatches = 'http://api.football-data.org/v2/competitions/2014/matches'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlmatches, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        matches = json.loads(r.text)['matches']
        sleep(11)
        partidos = []
        for i in matches:
            try:
                p = i['id']
                partidos.append(p)
            except:
                pass    
        for i in partidos:
            try:
                sleep(2)
                url = 'http://api.football-data.org/v2/matches/' + str(i)
                print('BUSCANDO EL PARTIDO CON URL %s' % url)
                r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
                print('---------------llamando API-----------------------')
                s = json.loads(r.text)['match']['substitutions']
                l = json.loads(r.text)['match']['homeTeam']['name']
                v = json.loads(r.text)['match']['awayTeam']['name']
                homelineup = json.loads(r.text)['match']['homeTeam']['lineup']
                awaylineup =  json.loads(r.text)['match']['awayTeam']['lineup']
                print('EL EKIPO LOCAL ES %s' % l)
                print('EL VISITANTE ES %s' % v)
                print('EL NUMERO DE CAMBIOS ES %s' % len(s))
                
                codigolocal = ''
                codigovisitante = ''
                localplayers = []
                visitorplayers = []            
                ls = []
                vs = []
                tl = []
                tv = []
                lg = []
                vg = []
                tlg = []
                lvg = []
              
                for h in homelineup:
                    codigolocal+=str(h['id'])
                
                for v in awaylineup:
                    codigovisitante+=str(v['id'])
                
                print('EL CODIGO LOCAL ES %s' % codigolocal)
                print('EL CODIGO VISITANTE ES %s' % codigovisitante)

                try:
                    local_lineup = Lineup.objects.get(lineupid=codigolocal)
                except:
                    players = []
                    local_lineup = Lineup.objects.create(lineupid=codigolocal, team= l)
                    for p in homelineup:
                        try:
                            player = Player.objects.get(name=str(p['id']))
                        except:
                            player = Player.objects.create(name = str(p['id']), team=l)
                            print('Creado el jugador %s' % i)
                        players.append(player) 
                    local_lineup.players = players
                    local_lineup.save()                                                     
                print('EL NOMBRE DE LA ALINEACION LOCAL ES %s' % local_lineup.lineupid)    
                                                        
                try:
                    visitor_lineup = Lineup.objects.get(lineupid=codigovisitante)
                except:
                    players = []
                    vistor_lineup = Lineup.objects.create(lineupid=codigolocal, team= v)
                    for p in visitorlineup:
                        try:
                            player = Player.objects.get(name=str(p['id']))
                        except:
                            player = Player.objects.create(name = str(p['id']), team=v)
                            print('Creado el jugador %s' % i)
                        players.append(player)  
                    visitor_lineup.players = players
                    visitor_lineup.save()                                                                                                           
               
                print('EL NOMBRE DE LA ALINEACION VISITANTE ES %s' % visitor_lineup.lineupid)    
                
                                                
                for i in s:
                    team = i['team']['name']    
                    if team == l:
                        ls.append(ls)
                    if team == v:
                        vs.append(vs)
         
                for i in ls:
                    time = i['minute']
                    tl.append(time)
                for i in vs:
                    time = i['minute']
                    tv.append(time)
            except Exception as e:
                print(e)
                pass
            
            print('los cambios locales son en %s y los visitantes en %s' % (tl,tv))    
           
            try:    
                goals = json.loads(r.text)['match']['goals']
                
                for i in goals:
                    team = i['team']['name']    
                    if team == l:
                        lg.append(ls)
                    if team == v:
                        vg.append(vs)
                        
                for i in lg:
                    time = i['minute']
                    tlg.append(time)
                for i in vg:
                    time = i['minute']
                    tvg.append(time)        
                    
                print('los cambios locales son en %s y los visitantes en %s' % (tlg, tvg))    
                
                tl.append(93)
                tv.append(93)
                localtimes = [y - x for x,y in zip(tl,tl[1:])]
                visitortimes = [y - x for x,y in zip(tv,tv[1:])]                  
                local_lineup.timeplayed  = local_lineup.timeplayed + tl[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION LOCAL %s' % tl[0])
                local_lineup.save()
                visitor_lineup.timeplayed = visitor_lineup.timeplated + tv[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION VISITANTE %s' % tv[0])
                visitor_lineup.save()
                
                print('AHORA VAMOS A AÑADIR LOS GOLES')
                
                #localgoaltimes = [y - x for x,y in zip(tlg,tlg[1:])]
                
                count = 0
                for goal in lgt:
                    if goal < tl[0]:
                        count+=1
                        local_lineup.goalsfavor = local_lineup.goalsfavor + 1 
                        localgoaltimes = localgoaltimes[1:]
                        visitor_lineup.goalscounter = visitor_lineup.goalscounter + 1
                        print(count)
                        print('GOL PRIMERA ALINEACION')
                        local_lineup.save()
                        visitor_lineup.save()
                        prinnt('QUITO GOL')
                    else:
                        print('GOLES DE OTRA ALINEACION')
             
            except Exception as e:
                print(e)
                pass#visitorgoaltimes = [y - x for x,y in zip(tvg,tvg[1:])]
            
            try:    
                count = 0
                for goal in visitortimes:
                    if goal < tv[0]:
                        count+=1
                        visitor_lineup.goalsfavor = visitor_lineup.goalsfavor + 1 
                        local_lineup.goalscounter = local_lineup.goalscounter + 1
                        visitorgoaltimes = localgoaltimes[1:]
                        local_lineup.save()
                        visitor_lineup.save()
                        print(count)
                        print('GOL PRIMERA ALINEACION')
                        print('QUITO GOL')
                    else:
                        print('GOLES DE OTRA ALINEACION')
            except Exception as e:
                print(e)
                pass
            
            print('AHORA ACTUALIZAMOS GOLES Y CAMBIOS EN EL EQUIPO LOCAL')
                
            try:
                count= 0
                for i in ls:
                    count+=1
                    limitsup = tl[count+1]
                    limitinf = tl[count]
                    tiempo = limitsup - limitinf
                    print('CREANDO LA ALINEACION QUE JUGÓ ENTRE MIN %s Y EL MIN  %s' % (limitinf,limitsup)) 
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigolocal = codigolocal.remove(sale)
                    codigolocal = codigolocal.append(entra)
                    for p in codigolocal:
                        try:
                            player = Player.objects.get(name=str(p))
                        except:
                            Player.objects.create(name = str(p), team=l)
                            print('Creado el jugador %s' % p)
                            player = Player.objects.get(name=str(p))                        
                        localplayers.append(player)
                    nueva, created = Lineup.objects.update_or_create(lineupid = codigolocal, players=codigolocal, team=l, timeplayed = localtimes[count])
                    nueva = Lineup.objects.get(lineupid=codigolocal)
                    for goal in localgoaltimes:
                        if goal in range(limitinf, limitsup):
                            nueva.goalsfavor = nueva.goalsfavor + 1
                            print('GOL AÑADIDO A FAVOR')
                    for goal in visitorgoaltimes:
                        if goal in range(limitinf, limitsup):
                            nueva.goalscounter = nueva.goalscounter + 1
                            print('GOL AÑADIDO EN CONTRA')        
                    nueva.save()            
                print('CREADA NUEVA LINEUP %s' % nueva.lineupid)
            except Exception as e:
                print(e)
                pass
            print('AHORA ACTUALIZAMOS GOLES Y CAMBIOS EN EL EQUIPO VISINTATE')

            try:
                count = 0
                for i in vs:
                    count+=1
                    limitsup = tv[count+1]
                    limitinf = tv[count]
                    tiempo = limitsup - limitinf
                    print('CREANDO LA ALINEACION QUE JUGÓ ENTRE MIN %s Y EL MIN  %s' % (limitinf,limitsup)) 
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigovisitante.remove(sale)
                    codigovisitante.append(entra)
                    for p in codigovisitante:
                        try:
                            player = Player.objects.get(name=str(p))
                        except:
                            Player.objects.create(name = str(p), team=v)
                            print('Creado el jugador %s' % p)
                            player = Player.objects.get(name=str(p))                        
                        visitorplayers.append(player)
                    nueva, created = Lineup.objects.ipdate_or_create(lineupid=codigovisitante, players=codigovisitante, team=v, timeplayed = tiempo)
                    nueva = Lineup.objects.get(lineupid=codigovisitante)
                    for goal in visitorgoaltimes:
                        if goal in range(limitinf, limitsup):
                            nueva.goalsfavor = nueva.goalsfavor + 1
                            print('GOL AÑADIDO A FAVOR')
                    for goal in localgoaltimes:
                        if goal in range(limitinf, limitsup):
                            nueva.goalscounter = nueva.goalscounter + 1
                            print('GOL AÑADIDO EN CONTRA')        
                    nueva.save()
                print('CREADA NUEVA LINEUP %s' % nueva.lineupid)
            except Exception as e:
                print(e)
                pass
            
        print('TERMINADAS TODAS LAS SUSTITUCIONES')                     
