"""
KIT103/KMA155 Programming Assignment 5: Permutations and Combinations
Submission script

Name: Shea Bunge
ID: 407095

Enter your answers to each question below either by replacing the
value None with a short piece of Python code that will calculate or
generate the answer or, in the case of Question 4, replacing the
body of the two functions with your implementation. After answering
a question run this script and test your implementation in the
IPython console.
"""

from itertools import combinations, permutations, product
from scipy.misc import comb, factorial


def fact(n):
	"""Returns the exact, integer value of n!"""
	return int(factorial(n, exact=True))


# Answers that can be calculated by single lines of code will be stored in
# this dictionary. Question 4's answers will be in the form of functions.
value_ans = {}

# Question 1: Permutations (1 mark)

value_ans['q1 a'] = 4 ** 3
value_ans['q1 b'] = {''.join(p) for p in product('AUGC', repeat=3)}
value_ans['q1 c'] = fact(5) // fact(5 - 3)
value_ans['q1 d'] = set(permutations(('cat', 'sat', 'hat', 'mat', 'pat'), 3))

# Question 2: Combinations (1 mark)

# If you use this list then your answers will be in the same order as the test program
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
students = {'Student %d' % i for i in range(1, 13)}

value_ans['q2 a'] = comb(len(rainbow), 2, exact=True)
value_ans['q2 b'] = set(combinations(rainbow, 2))
value_ans['q2 c'] = comb(len(students), 3, exact=True)
value_ans['q2 d'] = set(combinations(students, 3))

# Question 3: You choose which (2 marks)

from string import ascii_uppercase

titles = set(ascii_uppercase[:18])  # 'A' through 'R'
n_books = 18

value_ans['q3 a'] = set(combinations(titles, 5))
value_ans['q3 b'] = fact(n_books)
value_ans['q3 c'] = set(product(titles, repeat=3))
value_ans['q3 d'] = n_books ** 3


# Question 4: Words are mightier than the sword (1 mark)

def word_perms(word):
	"""Returns the set of all permutations of the letters in `word`."""
	# Question 4a: Generates all strings that are permutations of the letters in word
	return {''.join(w) for w in permutations(word)}


def anagrams(word):
	"""Returns the set of all anagrams of `word` (provided it is
	between 2 and 10 characters in length). Behaviour if it is shorter
	or longer than that is unspecified.
	"""
	# Question 4b: Generates all permutations of word and filters it to contain only valid words
	valid_words = word_sets[len(word)]
	return {w for w in word_perms(word) if w in valid_words}


# Needed for Question 4

from os.path import isfile


def load_words():
	name = 'words.2-10.txt'
	if isfile(name):
		all_words = [l.rstrip() for l in open(name, 'r')]
		as_lists = {}
		for size in range(2, 11):
			as_lists[size] = [word for word in all_words if len(word) == size]
		as_sets = {size: (set(words) if words else None) for size, words in as_lists.items()}
		return as_lists, as_sets
	return None, None


word_lists, word_sets = load_words()
# Usage examples (note that you do not necessarily need to use both word_lists and word_sets):
# word_lists[2] is a list of the two-letter words
# word_sets[9] is a set of the nine-letter words

# End of things needed for Question 4
