from flask import Flask

app = Flask(__name__)
app.config['DEBUG']=False
app.config['SECRET_KEY']='gpiocommander'
app.config['TESTING']=False
app.logger.disabled = True

from app import views

