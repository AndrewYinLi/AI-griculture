import sys
import os
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import numpy as np
import matplotlib.pyplot as plt

random_forest = new RandomForestClassifier(n_estimators = 200, n_jobs = -1);
mem = genfromtxt('sensor_baseline.csv', delimiter=',')

app = Flask(__name__)

@app.route('/')
def index():
	sensor_data = urllib.request.urlopen("HTTP_HERE").read().split(",")
	random_forest.fit(np.array(mem));
	prediction = random_forest.predict(sensor_data);
	mem = np.delete(mem, 0, 0)
	mem = np.append(mem, [prediction + sensor_data], axis=0)
	return render_template('index.html')