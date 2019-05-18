#!/usr/bin/python


#################################################################
#OBJECTIVE OF THE TASK

# Your program will read this data file and perform the following jobs:

# (1) Read all the data from file and save it into a Python dictionary. 
# Each key in the dictionary should be a country name as read from the file, 
# and value of that key will be a Python list containing emission data for that specific country. 
# Once all the file is read, dictionary will contain 195 keys Each key will 
# correspond to a Python list containing 14 numbers (emission data from 1996 to 2010). 
# You should use this dictionary for the next three jobs.

# (2) Calculate worldwide statistics (min, max, average) for a user-selected year. 
# See example in the sample-run below.

# (3) Extract data for up to three user-selected country and save it to a new file 
# Emissions_subset.csv. New file should have exactly same format as the 
# source file, i.e. first line of headers and then up to 3 lines for selected countries. 
# See the sample-run below for an example.


import csv

##################################################################

# TASK-1 (CSV to DICT)

reader = csv.reader(open('/home/saad/Desktop/Emissions.csv', 'r'))
pydict = {}
for row in reader:
	pydict[row[0]]=row[1:]

##################################################################




##################################################################

# TASK-2 (READING AVG,MIN,MAX from DICT)

def calc_average( year ):
	# open the file in universal line ending mode 
	with open('/home/saad/Desktop/Emissions.csv', 'rU') as infile:
	  # read the file as a dictionary for each row ({header : value})
	  reader = csv.DictReader(infile)
	  data = {}
	  for row in reader:
	    for header, value in row.items():
	      try:
	        data[header].append(value)
	      except KeyError:
	        data[header] = [value]

	li = data[str(year)]
	numbers_int = [float(x) for x in li]
	average = sum(numbers_int) / float(len(li))
	print "Average of the year selected is {}".format(average)
	maxim = max(numbers_int)
	minim = min(numbers_int)
	return maxim, minim

def max_and_min(maxim,minim):
	for key, value in pydict.iteritems():
		if str(maxim) in value:
			print key,maxim
		if str(minim) in value:
			print key,minim


print "***************************************************"
print "Program to analyze CSV and Calculate Stats from it"
print "***************************************************"
print "INPUT"
print "*****"
select_year=input("Select a year to find statistics (1997 to 2010):")
print "********************************************************"
print "OUTPUT"
print "**************************************************************"
for key, value in pydict.iteritems():
	if 'CO2 per capita' == key:
		if str(select_year) in value:
			maxim,minim = calc_average(select_year)
			max_and_min(maxim,minim)
		else:
			print 'sorry, that is not a valid year'

##################################################################





##################################################################

# TASK-3



##################################################################