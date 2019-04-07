import sys
import os
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
import threading
import requests
import datetime
import googleapiclient.discovery

microcontrollerIP = "http://172.31.32.74:3000/"

random_forest = RandomForestClassifier(n_estimators = 200, n_jobs = -1);
mem = np.genfromtxt("sensor_baseline.csv", delimiter=",").tolist()
cache = []
moistureShortPath = "moistureshort_test.png"
moistureLongPath = "moisturelong_test.png"
memGlobal = None
cacheGlobal = None

def predict_json(project, model, instances, version=None):
	"""Send json data to a deployed model for prediction.
	Args:
		project (str): project where the Cloud ML Engine Model is deployed.
		model (str): model name.
		instances ([[float]]): List of input instances, where each input
		   instance is a list of floats.
		version: str, version of the model to target.
	Returns:
		Mapping[str: any]: dictionary of prediction results defined by the
			model.
	"""
	# Create the ML Engine service object.
	# To authenticate set the environment variable
	# GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
	service = googleapiclient.discovery.build('ml', 'v1')
	name = 'projects/{}/models/{}'.format(project, model)

	if version is not None:
		name += '/versions/{}'.format(version)

	response = service.projects().predict(
		name=name,
		body={'instances': instances}
	).execute()

	if 'error' in response:
		raise RuntimeError(response['error'])

	return response['predictions']

def update(cache):
	memNp = np.array(mem)
	random_forest.fit(memNp[:, 1:], memNp[:, 0])
	pred = predict_json("plant-controller", "random_forest",[[46,590,14,25]], "random_forest_v1")
	print(pred)
	# global memGlobal
	# global cacheGlobal
	# if len(cache) > 0:
	# 	aggregate = np.array(mem + cache).astype(float).astype(int)
	# 	random_forest.fit(aggregate[:, 1:], aggregate[:, 0])
	# else:
	# 	memNp = np.array(mem)
	# 	random_forest.fit(memNp[:, 1:], memNp[:, 0])
	# sensor_data = requests.get(microcontrollerIP)._content.decode("utf-8").split(",")
	# prediction = random_forest.predict([sensor_data]);
	# if len(cache) > 1000:
	# 	del cache[0]
	# cache.append([prediction[0]] + sensor_data)
	# light = 0
	# currentDT = datetime.datetime.now()
	# if (currentDT.hour >= 6 and currentDT.hour < 9) or int(sensor_data[0]) < 50:
	# 	light = 1
	# requests.post(microcontrollerIP, data = {"pump":int(prediction[0]), "light":light})
	
	# memGlobal = mem
	# cacheGlobal = cache

	threading.Timer(2.0, update, [cache]).start()

app = Flask(__name__)
update(cache)

@app.route('/')
def index():
	# memNp = np.array(memGlobal)
	# cacheNp = np.array(cacheGlobal)
	# plt.title("Short-term Moisture")
	# plt.plot(np.array(range(1, cacheNp[:, 2].shape[0]+1)), cacheNp[:, 2], '-', color="g")
	# plt.xlabel("Seconds")
	# plt.ylabel("Analog Moisture Level")
	# if os.path.exists(moistureShortPath):
	# 	os.remove(moistureShortPath)
	# plt.savefig(moistureShortPath)
	# plt.clf()

	plt.title("Long-term Moisture")
	plt.plot(np.array(range(1, memNp[:, 2].shape[0]+1)), memNp[:, 2], '-', color="r")
	
	plt.xlabel("Seconds")
	plt.ylabel("Analog Moisture Level")
	if os.path.exists(moistureShortPath):
		os.remove(moistureShortPath)
	plt.savefig(moistureShortPath)
	plt.clf()

	plt.title("Long-term Moisture")
	plt.plot(np.array(range(1, memNp[:, 2].shape[0]+1)), memNp[:, 2], '-', color="r")
	
	plt.xlabel("Seconds")
	plt.ylabel("Analog Moisture Level")
	if os.path.exists(moistureLongPath):
		os.remove(moistureLongPath)
	plt.savefig(moistureLongPath)
	plt.clf()
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000)