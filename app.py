import sys
import os
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import threading

microcontrollerIP = "http://172.31.32.74:3000/"

random_forest = RandomForestClassifier(n_estimators = 200, n_jobs = -1);
mem = np.genfromtxt('sensor_baseline.csv', delimiter=',')
cache = np.array([])

def update(cache):
	threading.Timer(2.0, update, [cache]).start()
	if cache.shape[0] > 0:
		aggregate = np.append(mem, cache, axis=0)
		random_forest.fit(aggregate[:, 1:], aggregate[:, 0].reshape(-1,1).ravel())
	else:
		random_forest.fit(mem[:, 1:], mem[:, 0].reshape(-1,1).ravel())
	sensor_data = urllib.request.urlopen(microcontrollerIP).read().decode('utf-8').split(",")
	prediction = random_forest.predict([sensor_data]);
	if cache.shape[0] > 1000:
		cache = np.delete(cache, 0, 0)
	cache = np.append(cache, np.append(prediction, sensor_data, axis=0), axis=0)
	urllib.request.urlopen(microcontrollerIP, prediction)

app = Flask(__name__)
update(cache)




@app.route('/')
def index():

	return render_template('index.html')