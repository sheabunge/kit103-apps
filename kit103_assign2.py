'''
KIT103/KMA155 Programming Assignment 2: Logic
Submission script

Name: Replace with your name
ID: Replace with your student ID

Enter your answers to each question below by completing each function
or, in the case of Question 4a, filling in the Karnaugh map.
After answering a question run this script and test your implementation.
'''

# Question 1: Riding the Sine Wave

REJECT, FIND_ADULT, ACCEPT = 'Sorry, you cannot ride', 'Find an adult', 'You can ride'

def q1_sine_wave_check(height, age, has_adult):
    '''Returns one of three string messages depending on whether a
    person can ride the Sine Wave or not.
    Parameters:
    height - integer height in cm
    age - integer age in years
    has_adult - True iff the person is accompanied by an adult
    '''
    return REJECT


# Question 2: Implementing predicates as functions

def q2_a(a, b):
    return None

def q2_b(a, b, c, d):
    return None

def q2_c(a, b, c):
    return None

def q2_d(a):
    return None


# Question 3: Simplifying predicates

def q3_a(a, b):
    return None

def q3_b(a, b, c, d):
    return None

def q3_c(a, b, c):
    return None

def q3_d(a):
    return None


# Question 4: Simplifying a predicate using a Karnaugh map

#Part a: Letter Detector Karnaugh Map --- replace the appropriate 0 entries with 1 (representing True)
q4_kmap = [
#cd\ab
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

#Part b: The detector function
def q4_acme_letter_detector(a, b, c, d):
    '''Returns True iff the curves present resemble a letter, False otherwise.'''
    #Your task is to replace this with an equivalent but simpler expression.
    # If you wish to split your expression over multiple lines then use a
    # slash \ at the end of each line, as below.
    return (not a and not b and not c and d) or \
            (not a and not b and c and d) or \
            (not a and b and not c and not d) or \
            (not a and b and c and d) or \
            (a and not b and c and d) or \
            (a and b and c and d)

#End of answers
