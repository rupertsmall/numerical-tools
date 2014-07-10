#integration using simpsons rule

from math import *          #enable the use of functions defined in the math module

DENSITY = 200   #DENSITY serves similar function to the base length of prob1.1.py
                 #DENSITY will be an approximate density since need 2*n intervals.

def evaluate_function(func, a):
    func_at_a = eval(func.replace('x', str(a)))
    return func_at_a

def integrate(func, domain):
    start_val = float(domain.strip().split(',')[0])
    end_val = float(domain.strip().split(',')[1])
    if start_val == end_val:
        return 0
    else:
        sum = 0.0
        interval_len = float(end_val - start_val)
        int_gap = ceil(interval_len)                    #gap to calculate number of points needed to give density ~DENSITY
        num_eval_points = DENSITY*int_gap               #number of evaluation points is even since DENSITY is even
        epsilon = float(interval_len)/num_eval_points   #epsilon, the step-size for the infinitesimal summation
        evaluate_at = start_val
        counter = 0                                     #counter to keep track of which point is being evaluated
        while counter <= num_eval_points:
            if counter == 0 or counter == num_eval_points: 
                sum += (evaluate_function(func, evaluate_at))
            elif counter % 2:                       #if is odd
                sum += 4*(evaluate_function(func, evaluate_at))
            else:                                   #is even
                sum += 2*(evaluate_function(func, evaluate_at))
            evaluate_at += epsilon
            percentage_completed = (counter/(float(DENSITY)*interval_len))*100
            per_comp = '%3d%%' % int(percentage_completed)
            print '\b\b\b\b\b' + per_comp,
            counter += 1
        sum = (1/float(3))*(interval_len/(float(counter-1)))*sum     #apply simpson's rule
        return '\n%.3f' % sum

if __name__ == '__main__':          #only run this part if progam is called directly
    while True:     # main program loop
        function = raw_input('enter function:  ')
        evaluate = raw_input('enter domain for integral:  ')

        if ',' in evaluate:
            integral = integrate(function, evaluate)
            print str(integral)
        elif evaluate:
            domain = evaluate+','+evaluate
            integral = integrate(function, domain)
            print str(integral)
        else: break

