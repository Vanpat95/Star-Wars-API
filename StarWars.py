import requests
import json
from flask import Flask


app = Flask(__name__)

@app.route("/jedi") 
def index():
    

url = "https://swapi.dev/api/"
response = requests.get(url)