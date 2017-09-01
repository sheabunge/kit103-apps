from math import gcd
from kit103_assign3 import q3_coprime
from random import randrange

N_TESTS = 50
LIMIT = 10e2
PRINT_PASSED = True

for _ in range(N_TESTS):
	a, b = randrange(2, LIMIT), randrange(2, LIMIT)

	result = q3_coprime(a, b)
	actual = gcd(a, b) == 1

	if actual != result:
		print(f'Failure: coprime{a, b} should return {actual} instead of {result}')
	elif PRINT_PASSED:
		print(f'Success: coprime{a, b} = {result}')

