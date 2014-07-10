#program for finding the derivative of an arbitrary function
#uses the three-point formula

from math import *      #allow the user to enter functions defined in the maths module

NUM_POINTS = 200       #number of points per unit interval. of course, cannot exceed 10e308
h = sqrt(10e-15)

def evaluate_function(func, a):
    func_at_a = eval(func.replace('x', str(a)))
    return func_at_a


def evaluate_derivative(func, a):
    derivative = (evaluate_function(func, a + h) - evaluate_function(func, a - h))/(2*h)
    return derivative

#main program loop. Called only if program is executed directly.
#this allows the functions defined here to be loaded as modules later
if __name__ == '__main__':

    while True:
        increment = 1.0/NUM_POINTS
        function = raw_input('enter function:  ')
        evaluate = raw_input('enter domain for derivative:  ')
        if ',' in evaluate:
            start_val = float(eval(evaluate.strip().split(',')[0]))
            end_val = float(eval(evaluate.strip().split(',')[1]))
            evaluate_at = start_val
            pipe = raw_input('pipe output to file dsin_x.txt? (y/n)  ')
            if pipe == 'y':
                fp = open('dsin_x.txt','w')
                while evaluate_at <= end_val:
                    fp.write(str(evaluate_at) + '\t' + str(evaluate_derivative(function, evaluate_at)) + '\n')
                    evaluate_at += increment
                fp.close()
            else:
                while evaluate_at <= end_val:
                    print str(evaluate_at) + '\t' + str(evaluate_derivative(function, evaluate_at))
                    evaluate_at += increment

        elif evaluate:
            evaluate_at = float(eval(evaluate.strip()))
            print str(evaluate_derivative(function, evaluate_at))

        else: break
