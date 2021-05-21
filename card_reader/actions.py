from gpiozero import LED
from time import sleep
import json
from card_reader.monitor import *
from app.models import Log, Status, Setting, Simulation
import random
from django.db.models import Count
import requests

greenLED = LED(22)
redLED = LED(23)

def sendswipe(cardID):
    response = requests.post('http://192.168.2.179:8000/cardhandler/swipe/', data = {"card":cardID})

def red(state, time):
    if state=="on":
       redLED.on()
    if state=="off":
       redLED.off()
    
def green(state, time):
    if state=="on":
        greenLED.on()
    if state=="off":
        greenLED.off()

def updatestatus(state):
    record = Status.objects.first()
    if record:
        scriptjson = json.loads(record.current)
        record.current = json.dumps({"state": state, "script": scriptjson["script"]})
    else:
        scriptstring = json.dumps({"state": state, "script": "stop"})
        record = Status(current=scriptstring)
    record.save()

def readstatus():
    record = Status.objects.first()
    return record.current

def updatesettings(state):
    record = Setting.objects.first()
    if record:
        record.current = state
    else:
        record = Setting(current=state)
    record.save()

def readsettings():
    record = Setting.objects.first()
    return record.current

def updatescript(state):
    record = Simulation.objects.first()
    if record:
        record.script = state
    else:
        record = Simulation(script=state)
    record.save()

def readscript():
    record = Simulation.objects.first()
    return record.script

def updaterun(run):
    record = Status.objects.first()
    if record:
        statejson = json.loads(record.current)
        record.current = json.dumps({"state": statejson["state"], "script": run})
    else:
        statusstring = json.dumps({"state": "close", "script": run})
        print(statusstring)
        record = Status(current=statusstring)
    record.save()
    if run == "start":
        scriptrun()

def scriptrun():
    print("Run script")
    record = Simulation.objects.first()
    script = record.script
    scriptjson = json.loads(script)
    repeat = scriptjson["repeat"]
    print(repeat)
    print(scriptjson["script"])
    while repeat > 0:
        for command in scriptjson["script"]:
            if command["command"] == "swipe":
                sendswipe(command["card"])
            if command["wait"] == "rand1":
                sleep(random.randint(5, 30))
            elif command["wait"] == "rand2":
                sleep(random.randint(1, 10))
            elif command["wait"] == "rand3":
                sleep(random.randint(1, 3))
        repeat -= 1
        print(repeat)



