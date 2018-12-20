#!/usr/bin/python
import random 
import numpy as np
import normal
'''
max_move= 5

location= [0,0]

number_flights= 20

for flight in range(number_flights):
    location= random.randrange( (-1,1)*max_move) + location
    print location
'''
location= [0,0]  #initial location

def move_mosquito(location):
    new_location= []  
    for coord in location:
        new_location= new_location.append(location + location.append(round(normalvariate(0,5))))

#        new_location= new_location.append(location + location.append(round(np.random.normal(0,5))))
#giving me an error that i cant add nonetype to list
        
        return new_location
        print new_location

for i in range(0,10):
    print location
    location= move_mosquito(location)
#print location
    #location= location + (round(normalvariate(0,5)), round(normalvariate(0,5)))

   # have multiple locations; ;one mosquito produces mod=squiroes and they can die anywhere; probability of ddeath); consider a mosq class; needs location; chances to move= timestep***; increment age by 1 every tume they move: always age- optionally move bc random ____think about var names carefully  
