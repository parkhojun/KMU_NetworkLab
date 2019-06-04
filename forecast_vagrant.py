# -*- coding: utf-8 -*-
import os
import forecastio
from flask import Flask, request, Response
from slackclient import SlackClient

app = Flask(__name__)

FORECAST_TOKEN = '(본인의 일기예보 토큰)'

@app.route('/webhook', methods=['POST'])
def inbound():
  username = request.form.get('user_name')
  message = 'empty'
  channel_name = request.form.get('channel_name')
  channel_id = request.form.get('channel_id')
  username = request.form.get('user_name')
  text = request.form.get('text')

  if text == "날씨":
      message = forecast()
  else:
      print(username)
      message = username + " in " + channel_name + " says: " + text

  return Response(message), 200

def forecast():
  lat = 37.610056
  lng = 126.997130

  forecast = forecastio.load_forecast(FORECAST_TOKEN, lat, lng)
  byHour = forecast.hourly()
  return byHour.summary

@app.route('/', methods=['GET'])
def test():
    return Response('It works!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
