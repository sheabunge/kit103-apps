"""
KIT103/KMA155 Programming Assignment 3: Number Theory part 1
Submission script

Name: Shea Bunge
ID: 407095

Enter your answers to each question below by completing each
function. After answering a question run this script and test
your implementation in the IPython console.
"""


# Question 1: Divisibility of really, really big integers (2 marks)

def divisible_by_2(s):
	"""Returns True if the number represented by the string s is
	divisible by 2, False otherwise."""
	return int(s[-1]) % 2 == 0


def divisible_by_3(s):
	"""Returns True if the number represented by the string s is
	divisible by 3, False otherwise."""
	return sum(int(n) for n in s) % 3 == 0


def divisible_by_4(s):
	"""Returns True if the number represented by the string s is
	divisible by 4, False otherwise."""
	return sum(int(n) for n in s[-2:]) % 4 == 0


def divisible_by_11(s):
	"""Returns True if the number represented by the string s is
	divisible by 11, False otherwise."""

	m = []

	for i, n in enumerate(s):
		n = int(n)
		m.append(-n if i % 2 == 0 else n)

	return sum(m) % 11 == 0

# Question 2: GCD from a prime factorisations (2 marks)

from collections import Counter


def q2_factor_gcd(a, b):
	"""Returns gcd(a, b), calculated from their prime factorisations."""
	return None


# Question 3: Are a and b coprime (i.e., relatively prime)? (1 mark)

# Implement your additional helper function here

def q3_coprime(a, b):
	"""Returns True if a and b are coprime, False otherwise."""
	return None


# End of answers


# Provided functions

from math import floor, sqrt


def primes(n):
	primes = set(range(2, n + 1))
	for k in range(2, floor(sqrt(n)) + 1):
		if k in primes:
			primes.difference_update(range(k ** 2, n + 1, k))
	return primes


def primes_list(n):
	return sorted(primes(n))


def factor_list(n):
	factors = []
	iprimes = iter(primes_list(n))
	while n > 1:
		p = next(iprimes)
		while n % p == 0:
			n = n // p
			factors.append(p)
	return factors

# End of provided functions
