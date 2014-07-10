#program for finding the derivative of an arbitrary function
#uses the standard definition of the derivative

from math import *      #will allow user to enter functions defined in Python math module

NUM_POINTS = 200       #number of points per unit interval. of course, cannot exceed 10e308
EPSILON = .2*sqrt(10e-15) 

def evaluate_function(func, a):     #evaluate the user-defined function
    func_at_a = eval(func.replace('x', str(a)))
    return func_at_a


def evaluate_derivative(func, a):   #evaluate the derivative of func at the point a
    h = max(abs(a), EPSILON**(.5)) * EPSILON**(.5)
    derivative = (evaluate_function(func, a + h) - evaluate_function(func, a))/h
    return derivative

#main program loop
while True:
        increment = 1.0/NUM_POINTS
        function = raw_input('enter function:  ')
        evaluate = raw_input('enter domain for derivative:  ')
        if ',' in evaluate:
            start_val = float(evaluate.strip().split(',')[0])
            end_val = float(evaluate.strip().split(',')[1])
            evaluate_at = start_val     #iterated variable
            while evaluate_at <= end_val:
               print str(evaluate_at) + '\t' + str(evaluate_derivative(function, evaluate_at))
               evaluate_at += increment

        elif evaluate:
            evaluate_at = float(evaluate.strip())
            print str(evaluate_derivative(function, evaluate_at))

        else: break
