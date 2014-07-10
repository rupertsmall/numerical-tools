#center of mass of a sliced doughnut

from random import random
from math import pi,sin,cos,atan 

M=100000000         #number of samples
y_samples = 0       #samples which have been in correct y range
x_samples = 0       #samples which have been in correct x range

#do something random
def rand_r():
    return random()

def rand_theta():
    return pi*random() - pi/2

def rand_phi():
    return 2*pi*random()


def x_is_in(r, theta, phi): #check that x value is in correct domain
    x = (3+r*cos(phi))*cos(theta)
    if x>=1:
        return True
    else:
        return False

def y_is_in(r, theta, phi): #check that y value is in correct domain 
    y = (3+r*cos(phi))*sin(theta)
    if y>=-3:
        return True
    else:
        return False

#main function. N is the number of evaluations to make (at random points) withing the sliced doughnut
def monte_carlo(N):
    i=0
    actual_sample_size = 0
    x=y=0    
    while i<=N:
        r = rand_r()
        theta = rand_theta()
        phi = rand_phi()
        if x_is_in(r, theta, phi) and y_is_in(r, theta, phi):
            #print (3+r*cos(phi))*cos(theta), (3+r*cos(phi))*sin(theta), r*sin(phi) #temporary: to plot coordinates
            x += (3+r*cos(phi))*cos(theta)
            y += (3+r*cos(phi))*sin(theta)   
            actual_sample_size += 1
        i +=1
    print 'center of mass in x: ',x/float(actual_sample_size)
    print 'center of mass in y: ',y/float(actual_sample_size)
    print 'number of sample points: ',float(actual_sample_size)
monte_carlo(M)
