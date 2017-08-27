from kit103_assign2 import *

PRINT_PASSED = True

""" Question 1: Riding the Sine Wave """

tests = (
	(109, 4,  False, 'Sorry, you cannot ride'),
	(109, 4,  True,  'Sorry, you cannot ride'),
	(109, 6,  False, 'Sorry, you cannot ride'),
	(109, 6,  True,  'Sorry, you cannot ride'),
	(109, 10, False, 'Sorry, you cannot ride'),
	(109, 10, True,  'Sorry, you cannot ride'),
	(150, 4,  False, 'Sorry, you cannot ride'),
	(150, 4,  True,  'Sorry, you cannot ride'),
	(150, 6,  False, 'Find an adult'),
	(150, 6,  True,  'You can ride'),
	(150, 10, False, 'You can ride'),
	(150, 10, True,  'You can ride'),
	(201, 4,  False, 'Sorry, you cannot ride'),
	(201, 4,  True,  'Sorry, you cannot ride'),
	(201, 6,  False, 'Sorry, you cannot ride'),
	(201, 6,  True,  'Sorry, you cannot ride'),
	(201, 10, False, 'Sorry, you cannot ride'),
	(201, 10, True,  'Sorry, you cannot ride'),
)

failed = 0

for case in tests:
	*inputs, expected = case
	result = q1_sine_wave_check(*inputs)

	if result != expected:
		print(f'Failed: q1{inputs!r} = {result!r}. {expected!r} expected')
		failed += 1
	elif PRINT_PASSED:
		print(f'Passed: q1{inputs!r} = {result!r}')

if failed == 0:
	print('✓ All tests passed!')
else:
	print(f'Error: {failed} tests failed')
