from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.serializers import serialize
from app.models import Log
import json
from card_reader.actions import *
from card_reader.monitor import *
from datetime import datetime, timedelta 
from datetime import date
from django.http import JsonResponse
from django.utils import timezone
import time

def index(request):
    return HttpResponse("basic device index")

def command(request):
    action = json.loads(request.body)
    if action["command"]=="swipe":
       sendswipe(action["card"])

    actionlog(action["command"] +' '+ action["card"])
    return HttpResponse("command sent %s." % action)

def status(request):
    currentstatus = readstatus()
    return HttpResponse("Status %s." % currentstatus)

def devsettings(request):
    if request.method == 'GET':
        currentsettings = readsettings()
    elif request.method == 'POST':
        sentsettings = json.loads(request.body)
        updatesettings(sentsettings)
        currentsettings = readsettings()

    return HttpResponse("settings %s." % currentsettings)

def monitor(request):
    if request.body:
        range = json.loads(request.body)
        starttime = range["start"]
        endtime = range["end"]
        monitorlog = Log.objects.filter(event_date__gte=starttime, event_date__lte=endtime)
        logoutput = serialize('json', monitorlog)
    else:
        monitorlog = Log.objects.filter(event_date__gte=datetime.now(tz=timezone.utc)+ timedelta(hours=-1))
        logoutput = serialize('json', monitorlog)

    return HttpResponse("monitor log %s." % logoutput)

def simulation(request):
    sentscript = json.loads(request.body)
    updatescript(json.dumps(sentscript))
    currentscript = readscript()
    return HttpResponse("Script %s." % currentscript)

def start(request):
    currentstatus = updaterun("start")
    return HttpResponse("Status %s." % currentstatus)

def stop(request):
    currentstatus = updaterun("stop")
    return HttpResponse("Status %s." % currentstatus)

def stats(request):
    starttime=date.today()
    print(starttime)
    stats = list(Log.objects.filter(event_date__gte=starttime).extra({'hour': 'strftime("%%H", event_date )'}).order_by().values('hour').annotate(count=Count('id')))
    return JsonResponse(stats, safe=False)
