# GA_ReliefShelter
An application that operates through a terminal and employs a genetic algorithm to identify the best 'p' sites for establishing relief shelters during floods. The algorithm considers various factors such as latitude, longitude, population, and projected duration of submergence. It addresses conflicting goals, such as maximizing a metric called population score and minimizing the average distance to the nearest shelter, while ensuring that the overall cost remains within the allocated budget.

## Constraints:

* The allocated budget is B crores.
* The accumulated population should be less than or equal to K times the current population.
* The number of days of submergence for a specific location (x) should be greater than or equal to the maximum number of submerged days among all other locations (y).
* The number of days of submergence for a specific location (x) should be greater than 0.

## Objectives:

* O1: Achieve the highest population score, which represents the number of individuals saved.
* O2: Minimize the average distance to the nearest relief shelter.
* O3: Optimize the cost to stay within the allocated budget while maximizing its value.

## Objective Function/Fitness function:
F= (O1 + O3 )/O2

## Implementation
* my dataset folder has the initial data set collected from a government website. It contains information about the towns and villages in all the districts of Kerala.
* gascript.py is the python script to extract data from the csv files in the above stated folder and the number of days before submerging and cost have been generated randomly. The reason for random generation is that this data is dynamic and can only be available in case of an actual calamity at that place.
* Now the problem we faced was that geopy was returning empty geocodes for certain locations due to the server being unable to handle too many requests. So we added the latitude and longitude in the dataset file itself. The python script used for this was lat_lan_add_script.py
* The final dataset that is used as input in out GA code is in dataset2.csv (generated using the above stated python script)
* Our main GA code is in main.py
* Our final population's best chromosome is plotted on map and is stored in index.html
* Also, the GA code, after running completely plots a graph of average fitness over generations as shown below:

![graph](https://user-images.githubusercontent.com/31369977/47575320-77cf6080-d95f-11e8-8979-7bf4a6a859ee.png)


## This is how index.html looks like:
![image](https://github.com/pritam825/ReliefShelter_GA_Optimization/assets/54195688/f8384f27-a62d-4d58-8790-c94f875a1d98)
