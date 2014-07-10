#program for finding the derivative of an arbitrary function
#this program asks the user to choose between the standard formula or the three-point formula, or compare, which outputs both

from math import *

NUM_POINTS = 200       #number of points per unit interval. of course, cannot exceed 10e308
EPSILON = .2*sqrt(10e-15)

def evaluate_function(func, a):
    func_at_a = eval(func.replace('x', str(a)))
    return func_at_a


def evaluate_derivative(func, a, m):
    h = max(abs(a), EPSILON**(.5)) * EPSILON**(.5)
    if method == 's':
        derivative = (evaluate_function(func, a + h) - evaluate_function(func, a))/h
        return derivative
    elif method == '3':
        derivative = (evaluate_function(func, a + h) - evaluate_function(func, a - h))/(2*h)
        return derivative
    elif method == 'c':
        derivative_standard = (evaluate_function(func, a + h) - evaluate_function(func, a))/h
        derivative_three_point = (evaluate_function(func, a + h) - evaluate_function(func, a - h))/(2*h)
        return derivative_standard, derivative_three_point
    else: return 'unknown method'

#main program loop
while True:
        increment = 1.0/NUM_POINTS
        function = raw_input('enter function:  ')
        evaluate = raw_input('enter domain for derivative:  ')
        method = raw_input('which method? \n(s)tandard \n(3) point formula \n(c)ompare both methods: ')
        
        if ',' in evaluate:
            start_val = float(evaluate.strip().split(',')[0])
            end_val = float(evaluate.strip().split(',')[1])
            evaluate_at = start_val
            while evaluate_at <= end_val:
               print str(evaluate_at) + '\t' + str(evaluate_derivative(function, evaluate_at, method))
               evaluate_at += increment

        elif evaluate:
            evaluate_at = float(evaluate.strip())
            print '%.30f' % evaluate_derivative(function, evaluate_at, method)

        else: break
