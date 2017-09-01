from random import randrange


def random_tests(func_name, test, expected, n_inputs=1, n_tests=50, min=1, max=None, print_passed=False):

	for _ in range(n_tests):
		inputs = [randrange(min, max) for _ in range(n_inputs)]

		result = test(*inputs)
		actual = expected(*inputs)

		if actual != result:
			print(f'Failure: {func_name}{tuple(inputs)} should return {actual} instead of {result}')
		elif print_passed:
			print(f'Success: {func_name}{tuple(inputs)} = {result}')

