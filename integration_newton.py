#Root finding and optimization (using newtons method)

from math import sqrt

#HARD-WIRED CONSTANTS
function = ''       #empty function string to hold the polynomial
CLOSE_ENOUGH = 20   #when seeding newtons method, how close to the x axis is close enough
MARGIN = 10e-5      #close enough to be a root
h = sqrt(10e-15)    #step for evaluating derivative
iterations = 100    #how many iterations of newton's law to use before stopping
min_gap = 10e-6     #minimum distance between roots


#GET USER-DEFINED COEFFICIENTS
coefficients = [0]  #quasi-empty list to hold coefficients
search_range = int(raw_input('\n\t\tsearch for roots in real/complex square of\n\t\tdomain (-a,+a) where a is an integer\n\n\
Enter value for a: '))
num_coefficients = int(raw_input('enter the degree of the polynomial: '))

for eachnum in range(num_coefficients):
    request = 'enter coefficient %d: ' % (eachnum+1)
    coefficients.append(float(raw_input(request)))

coefficients[0] = float(raw_input('enter additive constant: '))

#generate the polynomial string from the coefficients
for eachnum in range(num_coefficients + 1):
    function = function + str(coefficients[eachnum]) + '*x**' + str(eachnum) + ' + '

function = function[0:len(function) - 2]

#tell the user what s/he entered
print '-'*80
print 'polynomial is: ',function
print '-'*80

def evaluate_function(func, a):     #evaluate the user-defined polynomial
    func_at_a = eval(func.replace('x', '('+str(a)+')'))
    return func_at_a

def evaluate_derivative(func, a):
    derivative = (evaluate_function(func, a + h) - evaluate_function(func, a - h))/(2*h)
    return derivative

def seeds(function):                #find approximate location of roots
    real = 0
    seed_vals = []
    while real <= search_range:
        imaginary = 0
        while imaginary <= search_range:
            equals = []         #roughwork tuple
            eval_point_1 = complex(real, imaginary)
            eval_point_2 = complex(-1*real, imaginary)
            eval_point_3 = complex(real, -1*imaginary)
            eval_point_4 = complex(-1*real, -1*imaginary)
            for eachnum in range(4):
                equals.append(evaluate_function(function, eval('eval_point_' + str(eachnum + 1))))
            for index in range(4):
                if abs(equals[index]) <= CLOSE_ENOUGH: seed_vals.append(eval('eval_point_' + str(index+1))) 
            imaginary += 1
        real += 1
    return seed_vals

def checker(root):
    #function to check that root is indeed a root
    if abs(evaluate_function(function,root)) < MARGIN:
        return True
    else:
        return False


def next_x(x):              #what is the next value of x in the newton's method sequence
    next_x_val = x - (evaluate_function(function, x))/(evaluate_derivative(function, x))
    return next_x_val

def newtons_method(seed_vals):  #given seeds, what are the roots
    roots = []                  #empty tuple to hold the roots

    for eachseed in seed_vals:
        n = 1                   #iteration count number
        while n <= iterations:
            eachseed = next_x(eachseed)
            n +=1
        roots.append(eachseed)

    return roots

#MAIN PROCESS-LOGIC
seed_vals = seeds(function)
roots = newtons_method(seed_vals)

#remove duplicates
for eachindex in range(len(roots)):
    for otherindex in range(len(roots)): 
        if roots[eachindex] != 'delete' and roots[otherindex] != 'delete':
            if abs(roots[eachindex] - roots[otherindex]) < min_gap and eachindex != otherindex:
                roots[otherindex] = 'delete'        #can't actually just delete at this point as deletion changes the length
                                                    #of the tuple which subsequently makes calls to higher indices out of range

j=1 #counter
for i in range(len(roots)):
    if roots[i] != 'delete' and checker(roots[i]):
        print 'root '+str(j)+': '+ str(roots[i])
        j +=1
            
#END
