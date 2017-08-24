"""
KIT103/KMA155 Programming Assignment 2: Logic
Submission script

Name: Shea Bunge
ID: 407095

Enter your answers to each question below by completing each function
or, in the case of Question 4a, filling in the Karnaugh map.
After answering a question run this script and test your implementation.
"""

# Question 1: Riding the Sine Wave

REJECT, FIND_ADULT, ACCEPT = 'Sorry, you cannot ride', 'Find an adult', 'You can ride'


def q1_sine_wave_check(height, age, has_adult):
	"""Returns one of three string messages depending on whether a
	person can ride the Sine Wave or not.
	Parameters:
	height - integer height in cm
	age - integer age in years
	has_adult - True iff the person is accompanied by an adult
	"""
	if 110 > height or height > 200 or age < 6:
		return REJECT

	if 6 <= age <= 9 and not has_adult:
		return FIND_ADULT

	return ACCEPT


# Question 2: Implementing predicates as functions

def q2_a(a, b):
	# ¬(a ∧ b) ∧ (a ∨ b)
	return not (a and b) and (a or b)


def q2_b(a, b, c, d):
	# a ∨ (¬b ∨ ¬c ∨ ¬d)
	return a or (not b or not c or not d)


def q2_c(a, b, c):
	# (a ∨ b) ∧ (a ∨ c)
	return (a or b) and (a or c)


def q2_d(a):
	# a ∧ ¬a
	return a and not a


# Question 3: Simplifying predicates

def q3_a(a, b):
	# a ⊕ b
	return a ^ b


def q3_b(a, b, c, d):
	# a ∨ ¬(b ∧ c ∧ d)
	return a or not (b and c and d)


def q3_c(a, b, c):
	# a ∨ b ∧ c
	return a or b and c


def q3_d(a):
	return False


# Question 4: Simplifying a predicate using a Karnaugh map

# Part a: Letter Detector Karnaugh Map --- replace the appropriate 0 entries with 1 (representing True)
q4_kmap = [
	# cd\ab
	[0, 1, 0, 0],
	[1, 0, 0, 0],
	[1, 1, 1, 1],
	[0, 0, 0, 0]
]


# Part b: The detector function
def q4_acme_letter_detector(a, b, c, d):
	"""Returns True iff the curves present resemble a letter, False otherwise."""
	return (c and d) or (not a and not b and d) or (not a and b and not c and not d)

# End of answers
