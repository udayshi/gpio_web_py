from flask import render_template
from app import app
from flask import jsonify
import os
import yaml
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route('/')
@app.route('/index')
def index():
   configs=getConfigs();
   for i in range(len(configs['devices'])):
       if getPinStatus(configs['devices'][i]['pin_id']):
           configs['devices'][i]['button']='success'
       else:
           configs['devices'][i]['button']='danger'
    
   return render_template("index.html",configs=configs)

@app.route('/api/toggle/<gpio_id>')
def api(gpio_id):
    return togglePin(gpio_id)


def getConfigs():
        return yaml.load(open(os.path.dirname(__file__)+"/../config/config.yml"))

def togglePin(WHICH_PIN):
    WHICH_PIN=int(WHICH_PIN)
    GPIO.setup(WHICH_PIN,GPIO.OUT)
    GPIO.output(WHICH_PIN,not GPIO.input(WHICH_PIN))

    if GPIO.input(WHICH_PIN):
 	status={'status':'ON'}
    else:
   	status={'status':'OFF'}
    return jsonify(status)

def getPinStatus(WHICH_PIN):
    WHICH_PIN=int(WHICH_PIN)
    GPIO.setup(WHICH_PIN,GPIO.OUT)
    return GPIO.input(WHICH_PIN)
