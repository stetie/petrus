#!/usr/bin/python

import re, os, time
from array import *
import petrusPlotter

def read_sensor(sensor_id):
	value = 0
	try:
		f = open("/sys/bus/w1/devices/{id}/w1_slave".format(id=sensor_id))
		f.readline()
		line = f.readline()
		value = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
		if value:
			value = float(value.group(2)) / 1000.0
		f.close()
	except (IOError), e:
		print e
	return value

def writeCSVline(temp, datadir):
	Y = time.strftime("%Y", time.gmtime())
	m = time.strftime("%m", time.gmtime())
	d = time.strftime("%d", time.gmtime())
	H = time.strftime("%H", time.gmtime())
	Min = time.strftime("%M", time.gmtime())
	datestr = time.strftime("%d-%m-%Y", time.gmtime())
	filename = datadir + datestr + ".csv"
	newfile = False
	if not (os.path.exists(filename)):
		f = open(filename, 'w')
		f.write("Year,Month,Day,Hour,Minute,Temperature\n")
		newfile = True
	else:
		f = open(datadir + datestr + ".csv", 'a')
	f.write("{0},{1},{2},{3},{4},{5}\n".format(Y, m, d, H, Min, temp))
	f.close()
	return newfile



sensors = os.listdir('/sys/bus/w1/devices')
sensors.remove('w1_bus_master1')
datadir = '/home/pi/petrus/data/'

temps = array('f', [0, 0, 0, 0, 0, 0])

while (True):
	for n in range(0, len(temps)):
		for sensor in sensors:
			temps[n] = read_sensor(sensor)
			#print temps[n]
			if n == (len(temps)-1):
				# Mittelwert berechnen und speichern
				mean = sum(temps)/float(len(temps))
				if writeCSVline(round(mean, 2), datadir):
					petrusPlotter.plotYesterday()
				petrusPlotter.plotToday()
			time.sleep(300)
			

