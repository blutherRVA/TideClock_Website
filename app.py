from flask import Flask, render_template, request, url_for
import weather_scraper


app = Flask(__name__)

#Latitude and longitude inputs
lat_ex = '37.5'
lon_ex = '-76.3'


@app.route('/')
def hello_world():
    return 'add /tidesHome'

@app.route('/weather')
def weather():
    return weather_scraper.weath(lat_ex, lon_ex)

@app.route('/tidesHome')
def tide_world():
    return render_template('tide.html')

