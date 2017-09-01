from random import randrange
import kit103_assign3 as assign3

PRINT_PASSED = False


def test(d, cases=20, limit=10):
	func = getattr(assign3, f'divisible_by_{d}')

	for _ in range(cases):
		n = randrange(limit) + 2
		divides = n % d == 0

		if func(str(n)) != divides:
			print(f'Failure: {n} should {"not " if divides else ""}be divisible by {d}')
		elif PRINT_PASSED:
			print(f'Success: {d} {" |" if divides else "!|"} {n}')


for d in (2, 3, 4, 11):
	test(d)
