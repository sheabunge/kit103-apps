"""
KIT103/KMA155 Programming Assignment 4: Number Theory part 2
Submission script

Name: Shea Bunge
ID: 407095

Enter your answers to each question below by assigning values
(or expressions to calculate values) to Question 1 and by
completing each function for Questions 2 and 3. You will need
to run this script after recording your student ID below in
order to find out what values you will decode in Question 1.
After answering parts of Questions 2 and 3 run this script
and test your implementation in the IPython console.
"""

# Question 1: Decode Linux Permissions (2 marks, *)

q1 = {}  # a dictionary of answers to Question 1; do not modify this initialisation


def sid2permissions(sid):
	"""Generates two octal triplets by converting the given integer
	student ID into octal, taking only the rightmost 6 digits if it
	is too long and padding with leading zeroes if it is too short,
	and then splitting the result into two halves.
	"""
	octid = oct(sid)[2:][-6:]  # remove 0o prefix, take last 6 digits
	octid = '0' * (6 - len(octid)) + octid  # pad if necessary
	return octid[:3], octid[3:]


# Task 1: Replace 0 with your student ID number (without leading zeroes)
q1['sid'] = 407095

# Do not modify the values assigned to these three entries
q1['both permissions'] = sid2permissions(q1['sid'])
q1['file A'] = q1['both permissions'][0]
q1['file B'] = q1['both permissions'][1]

# Task 2: Replace the Nones with your Question 1 answers here
q1['a-1 bitset'] = 0b100011011
q1['a-2 g+w?'] = q1['a-1 bitset'] & 0o020 > 0
q1['a-3 g+x?'] = q1['a-1 bitset'] & 0o010 > 0
q1['a-4 o+r?'] = q1['a-1 bitset'] & 0o004 > 0
q1['b-1 bitset'] = 0b000110111
q1['b-2 u+w?'] = q1['b-1 bitset'] & 0o200 > 0
q1['b-3 g+r?'] = q1['b-1 bitset'] & 0o040 > 0
q1['b-4 o+r?'] = q1['b-1 bitset'] & 0o004 > 0

# Question 2: base2base (1.5 marks, *)

from string import ascii_uppercase as capitals

digits = [str(i) for i in range(0, 10)] + [c for c in capitals[:26]]


# Declare any additional helper function here


def base2base(n, b1, b2):
	"""Converts n, a string representing a number in base b1, to a
	string representing the same value in base b2. 2 <= b1, b2 <= 36.
	"""
	return None


# Question 3: Really Stupid Encryption (RSE) (1.5 marks)

def encrypt(m):
	"""Encrypts the string message m using the smallest valid key
	(i.e., base) needed to encode the message, and returns both the
	encrypted message and base used.
	"""
	valid_m = clean(m)
	b = select_key(valid_m)
	return int(valid_m, b), b


# Question 3a
def select_key(m):
	"""Selects a key (i.e., base) that is just large enough to encrypt
	the given message in the RSE cryptosystem
	"""
	# Q3a: Modify this function to determine and return the smallest valid key
	return 36


# Question 3b
def decrypt(c, b):
	"""Decrypts the given integer message c by converting it to a
	string representing the same value in base b.
	"""
	# Q3b: Replace this implementation as specified in the assignment,
	#      including restoring spaces using with_spaces()
	return None


# Utility functions used by encrypt and decrypt
def clean(m):
	"""Returns a 'cleaned' version of the message m containing only
	valid symbols 0-9 and A-Z, with any spaces replaced by zero
	"""
	return ''.join([c for c in no_spaces(m).upper() if c in digits])


def no_spaces(m):
	"""Replaces spaces in the given plain text message with zeroes"""
	return m.replace(' ', '0')


def with_spaces(m):
	"""Replaces all instances of 0 in the given message with spaces"""
	return m.replace('0', ' ')


# Question 3c
def brute_force(c):
	"""Generates and returns a list of pairs of possible encryption bases
	and the plain text message that is recovered if there are used.
	"""
	# Q3c: Replace this implementation as specified in the assignment
	return [(10, c)]  # currently returns the original message only


def print_options(options):
	"""Pretty prints the list of decryption options"""
	print('key\tdecrypts to')
	for option in options:
		print(*option, sep='\t')

# End of answers
