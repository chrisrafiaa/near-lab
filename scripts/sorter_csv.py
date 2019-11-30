import os
from os import listdir
from os.path import isfile, join
import sys, csv, operator

data = csv.reader(open('sorted_names.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(4),reverse=True)    # 0 specifies according to first column we want to sort
#now write the sorte result into new CSV file
with open('sorted_names.csv', mode="w") as f:
	fileWriter = csv.writer(f, delimiter=',')
	for row in sortedlist:
		fileWriter.writerow(row)