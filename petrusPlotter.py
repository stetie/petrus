#!/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import pytz

from tzlocal import get_localzone

tz = get_localzone()

datadir = '/home/pi/petrus/data/'
graphdir = '/home/pi/petrus/graph/'
today = datetime.datetime.utcnow()
todaystr = today.strftime("%d-%m-%Y")
data = np.loadtxt(datadir + todaystr + ".csv", skiprows=1, delimiter=',')

dates = list()

for d in data:
	dates.extend([datetime.datetime(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]), 0, tzinfo=pytz.utc).astimezone(tz)])

plt.plot(dates, data[:, 5], 'o-')
plt.xlabel('Zeit')
plt.ylabel('Temperatur (C)')
plt.savefig(graphdir + todaystr + ".png")
