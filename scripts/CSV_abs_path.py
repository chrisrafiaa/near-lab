import os
from os import listdir
from os.path import isfile, join
import sys, csv, operator

###############VARIABLES TO INITIALIZE###############
# path to get abs paths from
# mypaths=['/Users/chrisrafiaa/Desktop/lab_stuff/MINC/MINC_t1/WTxWT_t1/preprocessed_minc', \
# '/Users/chrisrafiaa/Desktop/lab_stuff/MINC/MINC_t2/WTxWT_t2/preprocessed_minc', \
# '/Users/chrisrafiaa/Desktop/lab_stuff/MINC/MINC_t3/WTxWT_t3/preprocessed_minc', \
# '/Users/chrisrafiaa/Desktop/lab_stuff/MINC/MINC_t4/WTxWT_t4/preprocessed_minc']
mypaths=['/data/near/chris/studies/cfowler_data/NFTII/NFTII_t1/WTxWT_t1', \
'/data/near/chris/studies/cfowler_data/NFTII/NFTII_t2/WTxWT_t2', \
'/data/near/chris/studies/cfowler_data/NFTII/NFTII_t3/WTxWT_t3', \
'/data/near/chris/studies/cfowler_data/NFTII/NFTII_t4/WTxWT_t4']
#file extensions to extract only
endswith='.nii'
#csv file name
csv_name1='unsorted.csv'
csv_name2='sorted_names.csv'
###############VARIABLES TO INITIALIZE###############
#Directory to store CSV file
curr_directory=os.getcwd()
full_paths=[]
for i in mypaths:
	os.chdir(i) #change directory to directories of myPath
	for f in listdir(i):
		if isfile(join(i, f)):
			full_paths+=[join(i,f)]

os.chdir(curr_directory)
full_paths.sort()
with open(csv_name1, mode='w') as csv_file:
	writer = csv.writer(csv_file,delimiter=',')
	#1st colm: all absolute path
	#writer.writerow(["Time1",'Time2','Time3','Time4','ID'])
	for i in full_paths:
		# writer.writerow([i])
 		writer.writerow([i,'','','',i.split("/")[-1][18:22]])


data = csv.reader(open(csv_name1),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(4),reverse=True)    # 0 specifies according to first column we want to sort
#now write the sorted result into new CSV file
with open(csv_name2, mode="w") as f:
	fileWriter = csv.writer(f, delimiter=',')
	for row in sortedlist:
		fileWriter.writerow(row)
