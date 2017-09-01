from math import gcd as real_gcd
from kit103_assign3 import q2_factor_gcd as gcd
from random import randrange

N_TESTS = 50
LIMIT = 10e5
PRINT_PASSED = True

for _ in range(N_TESTS):
	a, b = randrange(2, LIMIT), randrange(2, LIMIT)

	result, actual = gcd(a, b), real_gcd(a, b)

	if gcd(a, b) != real_gcd(a, b):
		print(f'Failure: gcd{a, b} returns {result} when it should return {actual}')
	elif PRINT_PASSED:
		print(f'Success: gcd{a, b} = {result}')
