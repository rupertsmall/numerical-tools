#numeric integration using the 2-point trapezoidal rule

from math import *

EPSILON = .0001  #base length of trapezoids

def evaluate_function(func, a):
    func_at_a = eval(func.replace('x', str(a)))
    return func_at_a

#doesnt yet take into account ability of domain a,b to have b<a
def integrate(func, domain):
    start_val = float(domain.strip().split(',')[0])
    end_val = float(domain.strip().split(',')[1])
    sum = 0.0
    interval_len = float(end_val - start_val)   # in case of flooring
    evaluate_at = start_val
    if start_val == end_val:
        return 0
    else:
        while evaluate_at < end_val:
            sum += EPSILON*(evaluate_function(func, evaluate_at) + evaluate_function(func, evaluate_at + EPSILON))*.5
            evaluate_at += EPSILON
            length_completed = evaluate_at - start_val
            percentage_completed = (length_completed/interval_len)*100
            per_comp = '%3d%%' % int(percentage_completed)
            print '\b\b\b\b\b' + per_comp,
        return '%.3f' % sum

while True:     # main program loop
        function = raw_input('enter function:  ')
        evaluate = raw_input('enter domain for integral:  ')
        
        if ',' in evaluate:
            integral = integrate(function, evaluate)
            print '\n'+str(integral)
        elif evaluate:
            domain = evaluate+','+evaluate
            integral = integrate(function, domain) 
            print str(integral)
        else: break

