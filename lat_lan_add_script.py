import os
import glob
import geopy.geocoders
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="GA")
from geopy.exc import GeocoderTimedOut
from geopy import distance
geopy.geocoders.options.default_timeout = 40
import csv
import random
import csv

output_file_path = 'output.csv'

with open(output_file_path, 'w', encoding='utf-8') as ofile:
	data_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Rest of your code goes here...

    # Your code here...



    # Rest of your code goes here...

	data_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for filepath in glob.glob(os.path.join('C:/Users/pritam/Desktop/BTech Project 2/GA_ReliefShelter-master/my dataset','*.csv')):
		with open(filepath) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count<50:
					if list({row[10]})[0] in ['Rural']: 
						var=geolocator.geocode(list({row[9]})[0])
						if var is not None:	
							data_writer.writerow([list({row[9]})[0],list({row[12]})[0],random.randint(1,20), round(random.uniform(0, 15), 1), var, var.latitude, var.longitude])					
							line_count+=1
		
		

		
		
