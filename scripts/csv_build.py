'''
Makes a dictionary with the IDs are the rat IDs
and the value a list of all the absolute directories
relevant to that rat.
'''
import csv

###VARIABLES TO EDIT###
csv_read = 'sorted_names 2.csv'
csv_write = 'DBM_input.csv'
#######################
reader = csv.reader(open(csv_read))
result = {}

# going through the rows of the csv
# and placing all rats with same ID into one row
# in a dictionary with the format {ID:[lst of paths]}

for row in reader:
    idx = row[4]
    value = row[0]
    if idx in result:
        result[idx].append(value)
    else:
        result[idx] = [value]

#add padding so all rows have length 4
for key in result:
	for i in range(0,4-len(result[key])):
		result[key].append('')
# 	result[key].append(key) uncomment this if you want the IDs
#	to be present at the end as well
with open(csv_write,mode='w') as f:
	fileWriter=csv.writer(f,delimiter=",")
	for key in result:
		fileWriter.writerow(result[key])